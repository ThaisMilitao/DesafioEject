from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('signin', views.signin, name = 'signin'),
    path('<id>/editar-usuario', views.editar_usuario, name = 'editar-usuario'),
    path('logout', views.logout, name = 'logout'),
]