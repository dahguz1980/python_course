from django.shortcuts import render
from .models import Venta

# Create your views here.


def index(request):
    ventas = Venta.objects.all()
    datos = {"ventas": ventas}
    return render(request, "ventas/index_ventas.html", context=datos)
