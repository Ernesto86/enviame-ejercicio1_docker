from api.api_node import ConsumirApiNode
from api.crud import EmpresaListarView, EmpresaCrearView, EmpresaEditarView, EmpresaEliminarView, EmpresaFakerView
from django.urls import path

urlpatterns = [
    path("listar",EmpresaListarView.as_view(),name="empresa_listar"),
    path("crear/",EmpresaCrearView.as_view(),name="crear"),
    path("editar/<int:pk>/",EmpresaEditarView.as_view(),name="editar"),
    path("eliminar/<int:pk>/",EmpresaEliminarView.as_view(),name="eliminar"),
    path("empresas/faker/<int:n>/",EmpresaFakerView.as_view(),name="faker"),
    path("consumir/api/node/",ConsumirApiNode.as_view(),name="api_node"),

]
