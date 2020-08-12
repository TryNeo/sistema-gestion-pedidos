from django.urls import path
from apps.dbd.views.dashboard.views import *
from apps.dbd.views.categoria.views import *

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),

    path('categoria/',CategoriaListView.as_view(),name="categoria_list"),
    path('categoria/new/',CategoriaCreateView.as_view(),name="categoria_new"),
    path('categoria/edit/<int:pk>',CategoriaUpdateView.as_view(),name="categoria_edit"),
    path('categoria/delete/<int:pk>',CategoriaDeleteView.as_view(),name="categoria_delete"),

]
