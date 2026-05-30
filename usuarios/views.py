from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def login_ejecutivo(request):
    error_message = None
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redireccionamos a la página de inicio / dashboard ejecutivo
                return redirect('inicio')
            else:
                error_message = "Credenciales incorrectas."
        else:
            error_message = "Usuario o contraseña inválidos."
    
    return render(request, 'usuarios/login.html', {'error': error_message})