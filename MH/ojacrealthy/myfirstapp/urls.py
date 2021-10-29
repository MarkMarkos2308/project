from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),  # es glxavorna
    path('singup/', views.singup, name='singup'),  # es grancum@
    path('login/', auth_views.LoginView.as_view(template_name='myfirstapp/login.html'), name='login'),  # es login@
    path('profile/', views.user_profile, name='profile'),  # es profile-@
]