from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView, name='register'),
    path('login/', views.LoginView, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.LogoutView, name='logout'),
]