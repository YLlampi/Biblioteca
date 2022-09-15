from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Event, File, Sponsor
from .forms import FileForm, EventForm


# Create your views here.


def home(request):
    sponsors = Sponsor.objects.all()
    files = File.objects.all()
    context = {
        'files': files,
        'sponsors': sponsors
    }
    return render(request, 'domain/home.html', context)


def display_events(request):
    events = Event.objects.all()
    sponsors = Sponsor.objects.all()
    context = {
        'sponsors': sponsors,
        'events': events,
    }

    return render(request, 'domain/events.html', context)


@login_required(login_url='login')
def upload_file(request):
    form = FileForm()

    if request.method == "POST":
        form = FileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'domain/file_form.html', context)


@login_required(login_url='login')
def create_event(request):
    form = EventForm()

    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'domain/event_form.html', context)


def login_page(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Usuario no Encontrado')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuario o Contraseña incorrecta')

    context = {'page': page}
    return render(request, 'domain/login_register.html', context)


def logout_user(request):
    logout(request)

    return redirect('home')


def register_page(request):
    page = 'register'
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registration')

    context = {'page': page, 'form': form}
    return render(request, 'domain/login_register.html', context)
