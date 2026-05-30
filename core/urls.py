from django.contrib import admin
from django.urls import path, include
from dashboard import views
from usuarios import views as usuarios_views 
from reportes import views as reportes_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', usuarios_views.login_ejecutivo, name='login'), 
    
    # Dashboard (Inicio)
    path('', views.inicio, name='inicio'),
    path('reportes-mensuales/', views.reporte_mensual, name='reporte_mensual'),
    path('exportar/excel/', views.exportar_ventas_excel, name='exportar_ventas_excel'),
    path('comparativo/', views.dashboard_comparativo, name='dashboard_comparativo'),
    path('analitica/', views.analitica_avanzada, name='analitica_avanzada'),
    path('agente-guia/', views.agente_guia, name='agente_guia'),
    
    # Rutas para Catálogos y Ventas
    path('catalogos/', include('catalogos.urls')), 
    path('ventas/', include('ventas.urls')), 
    path('reportes/mensual/', views.reporte_mensual, name='reporte_mensual'),
    path('mercado/', views.lista_mercado, name='mercado'),
]