
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('associados/', views.associados_list, name='associados_list'),
    path('associados/novo/', views.associado_create, name='associado_create'),
    path('associados/<int:pk>/', views.associado_detalhes, name='associado_detalhes'),
    path('associados/<int:pk>/editar/', views.associado_edit, name='associado_edit'),
    path('associados/<int:pk>/excluir/', views.associado_delete, name='associado_delete'),
    path('associados/<int:pk>/financeiro/', views.financeiro_associado, name='financeiro_associado'),
    path('relatorios/', views.relatorios, name='relatorios'),
]
