"""
URL configuration for urban project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from productos import views
from django.conf import settings
from django.conf.urls.static import static
from productos.views import tienda  # Si la app se llama "productos"
from productos.views import perfil, editar_perfil




urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.index, name='index'),
    
    path('base/', views.base, name='base'),
    path('home/', views.home, name='home'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('mapanoti/', views.mapanoti, name='mapanoti'),
    path('galeria/', views.galeria, name='galeria'),
    path('carro_productos/', views.carro_productos, name='carro_productos'),
    path('carrito/', views.carrito, name='carrito'),
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro, name='registro'),
    path('logout/', views.logout_view, name='logout'),
    path('logout', views.logout_request, name='logout'),
    path('', tienda, name='tienda'),
    path('perfil/', views.perfil, name='perfil'),
    path("accounts/login/", LoginView.as_view(template_name="login.html"), name="login"),
    path('perfil/', perfil, name='perfil'),
    path('perfil/editar/', editar_perfil, name='editar_perfil'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)