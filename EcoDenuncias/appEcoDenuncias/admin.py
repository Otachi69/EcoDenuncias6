from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from appEcoDenuncias. models import *
# Register your models here.



@admin.register(Usuarios)
class UsuariosAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_active',)

@admin.register(Roles)
class RolesAdmin(admin.ModelAdmin):
    list_display = ('nombre_rol',)
    search_fields = ('nombre_rol',)
    
@admin.register(UsuarioRoles)
class UsuarioRolesAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'rol', 'estado_usuario_rol')
    search_fields = ('usuario__username', 'rol__nombre_rol', 'estado_usuario_rol')
    list_filter = ('estado_usuario_rol',)