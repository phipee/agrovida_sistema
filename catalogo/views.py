from django.shortcuts import render

def mostrar_productos(render):
    productos = [
    {"nombre": "Fertilizante NPK 15-15-15", "categoria": "Fertilizantes", "precio": 18990, "stock": 120},
    {"nombre": "Semilla de Maíz Híbrido", "categoria": "Semillas", "precio": 5990, "stock": 340},
    {"nombre": "Herbicida Glifosato 20L", "categoria": "Agroquímicos", "precio": 45990, "stock": 25},
    contexto = {'catalogo': catalogo}


    ]
    return render (request, 'index.html', contexto  )


    return render(request, 'pagina.html', contexto)
# Create your views here.
