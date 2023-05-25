from django.urls import path

from . import views

# *********** URLS basadas en funciones
# urlpatterns = [
#     path("", views.index, name="index"),
#     path("producto_categoria_listado/", views.producto_categoria_list, name="producto_categoria_list"),
#     path("producto_categoria_create/", views.producto_categoria_create, name="producto_categoria_create"),
#     path("producto_categoria_delete/<int:id>", views.producto_categoria_delete, name="producto_categoria_delete"),
#     path("producto_categoria_update/<int:id>", views.producto_categoria_delete, name="producto_categoria_delete"),
# ]

# *********** URLS basadas en clases
urlpatterns = [
    path("", views.index, name="index"),
    path("productocategoria/list/", views.ProductoCategoriaList.as_view(), name="productocategoria_list"),
    path("productocategoria/create/", views.ProductoCategoriaCreate.as_view(), name="productocategoria_create"),
    # ! De forma predeterminada, las URLs basadas en clases reciben pk, no id.
    path(
        "productocategoria/delete/<int:pk>", views.ProductoCategoriaDelete.as_view(), name="productocategoria_delete"
    ),
    # ! De forma predeterminada, las URLs basadas en clases reciben pk, no id.
    path(
        "productocategoria/update/<int:pk>", views.ProductoCategoriaUpdate.as_view(), name="productocategoria_update"
    ),
    path(
        "productocategoria/detail/<int:pk>", views.ProductoCategoriaDetail.as_view(), name="productocategoria_detail"
    ),
    path("list/", views.ProductoList.as_view(), name="producto_list"),
    path("create/", views.ProductoCreate.as_view(), name="producto_create"),
    path("delete/<int:pk>", views.ProductoDelete.as_view(), name="producto_delete"),
    path("update/<int:pk>", views.ProductoUpdate.as_view(), name="producto_update"),
     path("detail/<int:pk>", views.ProductoDetail.as_view(), name="producto_detail"),
]
