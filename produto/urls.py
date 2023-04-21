from django.urls import path
from . import views

urlpatterns = [
  path('dashboard', views.dashboard, name = 'dashboard'),
  path('meus-produtos', views.meus_produtos, name = 'meus-produtos'),
  path('registrar-produtos', views.registrar_produtos, name = 'registrar-produtos'),
  path('<id>/editar-produto', views.editar_produto, name = 'editar-produto'),
  path('<id>/deletar-produto', views.deletar_produto, name = 'deletar-produto'),

]