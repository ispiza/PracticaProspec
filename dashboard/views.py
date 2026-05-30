from datetime import datetime
from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth
from django.http import HttpResponse
from django.shortcuts import render
from ventas.models import Venta, DetalleVenta
from catalogos.models import Cliente
from scipy import stats

def inicio(request):
    ventas = Venta.objects.select_related('cliente', 'vendedor', 'metodo_pago', 'sucursal').all()
    total_ventas_valor = Venta.objects.aggregate(total=Sum('total'))['total'] or 0
    num_ventas = Venta.objects.count()
    num_productos = Venta.objects.values('detalles__producto').distinct().count()
    num_clientes = Cliente.objects.count()
    
    return render(request, 'dashboard/inicio.html', {
        'ventas': ventas,
        'total_ventas_valor': total_ventas_valor,
        'num_ventas': num_ventas,
        'num_productos': num_productos,
        'num_clientes': num_clientes
    })

def reporte_mensual(request):
    datos = Venta.objects.annotate(mes=TruncMonth('fecha')).values('mes').annotate(
        total_ventas=Sum('total'), total_documentos=Count('id')
    ).order_by('mes')
    return render(request, 'dashboard/reporte_mensual.html', {'datos': datos})

def exportar_ventas_excel(request):
    return HttpResponse("Exportación en proceso...")

def dashboard_comparativo(request):
    divisa = request.GET.get('divisa', 'MXN')
    factor = 0.05 if divisa == 'USD' else 1.0
    
    comparativo_categorias = DetalleVenta.objects.values('producto__categoria__nombre').annotate(total=Sum('importe')).order_by('-total')
    comparativo_ciudades = Venta.objects.values('sucursal__ciudad').annotate(total=Sum('total')).order_by('-total')
    comparativo_metodos = Venta.objects.values('metodo_pago__nombre').annotate(total=Sum('total')).order_by('-total')
    
    for lista in [comparativo_categorias, comparativo_ciudades, comparativo_metodos]:
        for item in lista:
            item['total'] = round(float(item['total'] or 0) * factor, 2)
    
    return render(request, 'dashboard/comparativo.html', {
        'comparativo_categorias': comparativo_categorias,
        'comparativo_ciudades': comparativo_ciudades,
        'comparativo_metodos': comparativo_metodos,
        'divisa': divisa
    })

def analitica_avanzada(request):
    ventas_por_sucursal = Venta.objects.values('sucursal__nombre').annotate(total=Sum('total'))
    grupos = [float(item['total'] or 0) for item in ventas_por_sucursal]
    
    contexto_anova = None
    if len(grupos) > 1:
        f_val, p_val = stats.f_oneway(*[[g] for g in grupos])
        contexto_anova = {
            'f_value': round(float(f_val), 4),
            'p_value': round(float(p_val), 4),
            'significativo': p_val < 0.05
        }
    
    return render(request, 'dashboard/analitica.html', {
        'anova': contexto_anova,
        'ventas_por_sucursal': ventas_por_sucursal,
        'nombres_sucursales': [s['sucursal__nombre'] for s in ventas_por_sucursal],
        'totales_ventas': [float(s['total']) for s in ventas_por_sucursal]
    })

def agente_guia(request):
    """
    Módulo para el Agente Guía Inteligente del SI Ejecutivo.
    """
    return render(request, 'dashboard/agente_guia.html', {
        'mensaje': "Bienvenido, estoy listo para asistirle con su análisis comercial."
    })
def lista_mercado(request):
   return render(request, 'dashboard/templates/dashboard/mercado/lista_mercado.html', {

   })