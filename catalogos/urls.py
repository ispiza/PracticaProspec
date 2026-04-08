from django.urls import path
from . import views

# Estas rutas definen a dónde irá el usuario cuando escriba /catalogos/...
urlpatterns = [
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('sucursales/', views.lista_sucursales, name='lista_sucursales'),
    path('vendedores/', views.lista_vendedores, name='lista_vendedores'),
    path('metodos_pago/', views.lista_metodos_pago, name='lista_metodos_pago'),
]