import os
import django
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from ventas.models import Venta
from catalogos.models import Cliente, Sucursal, Vendedor, MetodoPago, Producto, Categoria

def importar():
    archivo = os.path.join(os.getcwd(), 'Dashboard2021_50000_registros.xlsx')
    df = pd.read_excel(archivo)
    df = df.fillna('Sin dato')
    
    print(f"Iniciando carga de {len(df)} registros...")
    
    for index, row in df.iterrows():
        try:
            # 1. Obtener o crear catálogos básicos
            cliente, _ = Cliente.objects.get_or_create(nombre=str(row['Cliente']))
            sucursal, _ = Sucursal.objects.get_or_create(nombre=str(row['Empresa']))
            vendedor, _ = Vendedor.objects.get_or_create(nombre=str(row['Vendedor']), defaults={'sucursal': sucursal})
            metodo, _ = MetodoPago.objects.get_or_create(nombre=str(row['Forma de pago']))
            categoria, _ = Categoria.objects.get_or_create(nombre=str(row['Categoría']))
            
            # 2. Lógica segura para Producto (Evita UNIQUE constraint failed)
            codigo_prod = str(row.get('Codigo', 'N/A'))
            producto = Producto.objects.filter(codigo=codigo_prod).first()
            
            if not producto:
                producto = Producto.objects.create(
                    nombre=str(row['Producto']),
                    categoria=categoria,
                    codigo=codigo_prod,
                    precio=float(row.get('Precio', 0.0))
                )
            
            # 3. Lógica segura para Venta
            if not Venta.objects.filter(folio=str(row['Documento'])).exists():
                Venta.objects.create(
                    folio=str(row['Documento']),
                    fecha=row['Fecha'],
                    cliente=cliente,
                    sucursal=sucursal,
                    vendedor=vendedor,
                    metodo_pago=metodo,
                    producto=producto,
                    ciudad=str(row['Ciudad']),
                    provincia=str(row['Provincia']),
                    cantidad=int(row['Cantidad']),
                    moneda=str(row['Moneda']),
                    precio_unitario=float(row['Precio']),
                    total=float(row['Ventas'])
                )
            
            if (index + 1) % 1000 == 0:
                print(f"Progreso: {index + 1} registros procesados...")
                
        except Exception as e:
            print(f"Error en fila {index}: {e}")

    print("¡Proceso terminado con éxito!")

if __name__ == '__main__':
    importar()