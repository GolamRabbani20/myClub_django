from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.userLogin, name='user-login'),
    path("logout/", views.userLogout, name='user-logout'),
    path('register/', views.UserRegister, name='user-register'),
]