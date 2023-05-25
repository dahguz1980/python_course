from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from . import forms, models


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "producto/index.html")


# def producto_categoria_list(request):
#     categorias = models.ProductoCategoria.objects.all()
#     context = {"categorias": categorias}
#     return render(request, "producto/producto_categoria_list.html", context)


class ProductoCategoriaList(ListView):
    model = models.ProductoCategoria


# def producto_categoria_create(request):
#     if request.method == "POST":
#         form = forms.ProductoCategoriaForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("producto:index")
#     else:
#         form = forms.ProductoCategoriaForm()
#     return render(request, "producto/producto_categoria_create.html", {"form": form})


class ProductoCategoriaCreate(CreateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    success_url = reverse_lazy("producto:index")


# def producto_categoria_delete(request, id):
#     categoria = models.ProductoCategoria.objects.get(id=id)
#     if request.method == "POST":
#         categoria.delete()
#         return redirect("producto:producto_categoria_list")
#     return render(request, "producto/producto_categoria_delete.html", {"categoria": categoria})


class ProductoCategoriaDelete(DeleteView):
    model = models.ProductoCategoria
    success_url = reverse_lazy("producto:productocategoria_list")


# def producto_categoria_update(request, id):
#     categoria = models.ProductoCategoria.objects.get(id=id)
#     if request.method == "POST":
#         form = forms.ProductoCategoriaForm(request.POST, instance=categoria)
#         if form.is_valid():
#             form.save()
#             return redirect("producto:producto_categoria_list")
#     else:
#         form = forms.ProductoCategoriaForm(instance=categoria)
#     return render(request, "producto/producto_categoria_update.html", {"form": form})


class ProductoCategoriaUpdate(UpdateView):
    model = models.ProductoCategoria
    success_url = reverse_lazy("producto:productocategoria_list")
    form_class = forms.ProductoCategoriaForm


class ProductoCategoriaDetail(DetailView):
    model = models.ProductoCategoria
