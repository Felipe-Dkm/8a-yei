
from django.shortcuts import render, redirect
import json
import os
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import logout
from .models import Producto
from django.shortcuts import redirect
# Create your views here.
def index(request):
    if request.user.is_authenticated:
            return redirect ('home')
    return render(request, 'index.html')



def perfil(request):
    return render(request, 'perfil.html')


def editar_perfil(request):
    if request.method == "POST":
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil')  # Redirige al perfil después de editar
    else:
        form = UserChangeForm(instance=request.user)
    
    return render(request, 'editar_perfil.html', {'form': form})



def logout_request(request):
    logout(request)
    return redirect('index') 

def tienda(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/tienda.html', {'productos': productos})

def base(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def mapanoti(request):
    return render(request, "mapanoti.html")

def galeria(request):
    return render(request, "galeria.html")

def editar_perfil(request):
    return render(request, 'editar_perfil.html')

def carro_productos(request):
    productos = Producto.objects.all()  # Obtiene todos los productos
    return render(request, "carro_productos.html", {"productos": productos})

def carrito(request):
    return render(request, "carrito.html")

# Vista de login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if not username or not password:
            messages.error(request, 'Por favor, ingresa ambos campos.')
            return render(request, 'login.html')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')  # Redirige a la página principal
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')

    return render(request, 'login.html')

# Vista de registro
def registro(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Las contraseñas no coinciden.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'El correo ya está registrado.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya está en uso.')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            auth_login(request, user)  # Iniciar sesión automáticamente
            messages.success(request, "¡Registro exitoso!.")
            return redirect('login')  # Redirige a la página de login

    return render(request, 'registro.html')

# Vista de cierre de sesión (logout)
def logout_view(request):
    auth_logout(request)  # Cierra la sesión del usuario
    return redirect('login')  # Redirige a la página de login

