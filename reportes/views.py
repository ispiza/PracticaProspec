from django.shortcuts import render

def reporte_mensual(request):
    # Por ahora, enviamos una lista vacía para que la vista cargue sin errores
    context = {'reportes': []}
    return render(request, 'reportes/reporte_mensual.html', context)