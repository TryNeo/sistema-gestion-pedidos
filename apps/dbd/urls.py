from django.urls import path

from apps.acts.views import *
from apps.dbd.views.roles.views import *
from apps.dbd.views.cliente.views import *
from apps.dbd.views.producto.views import *
from apps.dbd.views.proveedor.views import *
from apps.dbd.views.dashboard.views import *
from apps.dbd.views.categoria.views import *
from apps.dbd.views.reportes.reporte_proveedor import *
from apps.dbd.views.reportes.reporte_producto import *
from apps.dbd.views.errors.views import *

urlpatterns = [
    #----------------------LOGIN-------------------------------------#
    path('', DashboardView.as_view(), name='dashboard'),

    #-----------------------CLIENTE---------------------------------# 
    path('cliente/',ClienteListView.as_view(),name="cliente_list"),
    path('cliente/new/',ClienteCreateView.as_view(),name="cliente_new"),
    path('cliente/edit/<int:pk>',ClienteUpdateView.as_view(),name="cliente_edit"),
    path('cliente/delete/<int:pk>',ClienteDeleteView.as_view(),name="cliente_delete"),

    #-----------------------CATEGORIA---------------------------------# 
    path('categoria/',CategoriaListView.as_view(),name="categoria_list"),
    path('categoria/new/',CategoriaCreateView.as_view(),name="categoria_new"),
    path('categoria/edit/<int:pk>',CategoriaUpdateView.as_view(),name="categoria_edit"),
    path('categoria/delete/<int:pk>',CategoriaDeleteView.as_view(),name="categoria_delete"),
    
    #-----------------------PROVEEDOR---------------------------------# 
    path('proveedor/',ProveedorListView.as_view(),name="proveedor_list"),
    path('proveedor/new/',ProveedorCreateView.as_view(),name="proveedor_new"),
    path('proveedor/edit/<int:pk>',ProveedorUpdateView.as_view(),name="proveedor_edit"),
    path('proveedor/delete/<int:pk>',ProveedorDeleteView.as_view(),name="proveedor_delete"),
    path('proveedor/consult/<int:pk>',ProveedorConsultView.as_view(),name="proveedor_consult"),

    #-----------------------PRODUCTO---------------------------------# 
    path('producto/',ProductoListView.as_view(),name="producto_list"),
    path('producto/new/',ProductoCreateView.as_view(),name="producto_new"),
    path('producto/edit/<int:pk>',ProductoUpdateView.as_view(),name="producto_edit"),
    path('producto/delete/<int:pk>',ProductoDeleteView.as_view(),name="producto_delete"),

    #-----------------------PEDIDO---------------------------------# 

    #-----------------------REPORTES---------------------------------# 
    path('reporte/proveedor/',ReporteProveedorPdf.as_view(),name="reporte_proveedor"),
    path('reporte/producto/',ReporteProductoPdf.as_view(),name="reporte_producto"),

    #----------------------SEGURIDAD------------------------------------#
    path('usuarios/',UserListView.as_view(),name="usuario_list"),
    path('usuarios/new/',UserCreateView.as_view(),name="usuario_new"),
    path('usuarios/edit/<int:pk>',UserUpdateView.as_view(),name="usuario_edit"),
    path('usuarios/delete/<int:pk>',UserDeleteView.as_view(),name="usuario_delete"),
    
    path('roles/',RolListView.as_view(),name="rol_list"),
    path('roles/new',RolCreateView.as_view(),name="rol_new"),
    path('roles/edit/<int:pk>',RolUpdateView.as_view(),name="rol_edit"),
    path('roles/delete/<int:pk>',RolDeleteView.as_view(),name="rol_delete"),
    
    path('403/',Error403View.as_view(),name="error_403"),

]

