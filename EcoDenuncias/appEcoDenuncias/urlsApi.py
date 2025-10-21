from django.contrib import admin
from django.urls import path
from .viewsApi import *
from appEcoDenuncias import viewsApi, views

urlpatterns = [
    path('usuario/', UsuariosList.as_view()),
    path('usuario/<int:pk>/', UsuariosDetail.as_view()),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('home/', views.dashboard_view, name='home'),

    path('rol/', RolesList.as_view()),
    path('rol/<int:pk>/', RolesDetail.as_view()),
    
    path('usuarioRol/', UsuarioRolesList.as_view()),
    path('usuarioRol/<int:pk>/', UsuarioRolesDetail.as_view()),
    
    path('territorial/', TerritorialesList.as_view()),
    path('territorial/<int:pk>/', TerritorialesDetail.as_view()),
    
    path('dependencia/', DependenciasList.as_view()),
    path('dependencia/<int:pk>/', DependenciasDetail.as_view()),
    
    path('municipios/', MunicipiosList.as_view()),
    path('municipios/<int:pk>/', MunicipiosDetail.as_view()),
    
    path('funcionario/', FuncionariosList.as_view()),
    path('funcionario/<int:pk>/', FuncionariosDetail.as_view()),
    
    path('requerimiento/', RequerimientosList.as_view()),
    path('requerimiento/<int:pk>/', RequerimientosDetail.as_view()),
    
    path('denuncia/', DenunciasList.as_view()),
    path('denuncia/<int:pk>/', DenunciasDetail.as_view()),
    
    path('solicitud/', SolicitudesList.as_view()),
    path('solicitud/<int:pk>/', SolicitudesDetail.as_view()),
    
    path('seguimiento/', SeguimientosList.as_view()),
    path('seguimiento/<int:pk>/', SeguimientosDetail.as_view()),
    
    path('respuesta/', RespuestasList.as_view()),
    path('respuesta/<int:pk>/', RespuestasDetail.as_view()),
    
    path('multimedia/', MultimediasList.as_view()),
    path('multimedia/<int:pk>/', MultimediasDetail.as_view()),
]