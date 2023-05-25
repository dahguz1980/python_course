from django.contrib import admin

from . import models

# admin.site.register(models.ProductoCategoria)


@admin.register(models.ProductoCategoria)
class ProductoCategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    search_fields = ("nombre",)
    list_filter = ("nombre",)
    ordering = ("nombre",)


@admin.register(models.Producto)
class Productodmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "productocategoria_id")
    search_fields = ("nombre",)
    list_filter = ("nombre",)
    ordering = ("nombre", "precio")
