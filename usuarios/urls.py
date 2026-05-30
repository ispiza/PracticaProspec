from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Esto le dice a Django: cuando alguien visite /usuarios/login/, muestra el login
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
]