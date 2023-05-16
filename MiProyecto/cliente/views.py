from django.shortcuts import render
from .models import Cliente

# Create your views here.


def index(request):
    clientes = Cliente.objects.all()
    datos = {"clientes": clientes}
    return render(request, "cliente/index_cliente.html", context=datos)
