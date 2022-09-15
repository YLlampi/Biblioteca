from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_page, name="register"),

    path('', views.home, name="home"),
    path('events/', views.display_events, name="events"),
    path('upload-file/', views.upload_file, name="uploadFile"),
    path('create-event/', views.create_event, name="createEvent")
]
