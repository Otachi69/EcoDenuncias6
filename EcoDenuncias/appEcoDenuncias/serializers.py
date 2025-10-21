from rest_framework import serializers
from .models import *


class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ['username', 'first_name', 'last_name', 'identificacion', 'email', 'telefono']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def create(self, validated_data):
        usuario = Usuarios(**validated_data)
        usuario.save()
        return usuario
        
class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'
       

class UsuarioRolesSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(queryset=Usuarios.objects.all())
    rol = serializers.PrimaryKeyRelatedField(queryset=Roles.objects.all())
    class Meta:
        model = UsuarioRoles
        fields = '__all__'


class TerritorialesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Territoriales
        fields = '__all__'

class MunicipiosSerializer(serializers.ModelSerializer):
    territorial = serializers.PrimaryKeyRelatedField(queryset=Territoriales.objects.all())
    
    class Meta:
        model = Municipios
        fields = '__all__'
        
    
class DependenciasSerializer(serializers.ModelSerializer):
    territorial = serializers.PrimaryKeyRelatedField(queryset=Territoriales.objects.all())
    
    class Meta:
        model = Dependencias
        fields = '__all__'


class FuncionariosSerializer(serializers.ModelSerializer):
    usuario = UsuariosSerializer()
    dependencia = serializers.PrimaryKeyRelatedField(queryset=Dependencias.objects.all())
    
    class Meta:
        model = Funcionarios
        fields = '__all__'
    
    
    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        usuario = UsuariosSerializer.create(**usuario_data)
        funcionario = Funcionarios.objects.create(usuario=usuario, **validated_data)
        return funcionario
    

class RequerimientosSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(queryset=Usuarios.objects.all())
    
    class Meta:
        model = Requerimientos
        fields =  ['tipo_requerimiento', 'estado', 'radicado']
        
        
class DenunciasSerializer(serializers.ModelSerializer):
    requerimiento = serializers.PrimaryKeyRelatedField(queryset=Requerimientos.objects.all())
    municipio = serializers.PrimaryKeyRelatedField(queryset=Municipios.objects.all())
    
    class Meta:
        model = Denuncias
        fields = ['municipio', 'fecha_denuncia', 'descripcion']

class SolicitudesSerializer(serializers.ModelSerializer):
    requerimiento = serializers.PrimaryKeyRelatedField(queryset=Requerimientos.objects.all())
    municipio = serializers.PrimaryKeyRelatedField(queryset=Municipios.objects.all())
    
    class Meta:
        model = Solicitudes
        fields = ['requerimiento', 'municipio', 'fecha_solicitud', 'descripcion']
        
class SeguimientosSerializer(serializers.ModelSerializer):
    requerimiento = serializers.PrimaryKeyRelatedField(queryset=Requerimientos.objects.all())
    funcionario = serializers.PrimaryKeyRelatedField(queryset=Funcionarios.objects.all())
    
    class Meta:
        model = Seguimientos
        fields = ['requerimiento', 'funcionario', 'fecha_seguimiento', 'actualizacion_reciente', 'dias_abierta','descripcion_actualizacion','tiempo_limite']
        
        
class RespuestasSerializer(serializers.ModelSerializer):
    seguimiento = serializers.PrimaryKeyRelatedField(queryset=Seguimientos.objects.all())
    
    class Meta:
        model = Respuestas
        fields = ['seguimiento', 'fecha_respuesta', 'descripcion_respuesta']


class MultimediasSerializer(serializers.ModelSerializer):
    requerimiento = serializers.PrimaryKeyRelatedField(queryset=Requerimientos.objects.all())
    
    class Meta:
        model = Multimedias
        fields = ['requerimiento', 'respuesta', 'multimedia']