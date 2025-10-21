from rest_framework import generics
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from .views import *
import threading




class UsuariosList(generics.ListCreateAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer
    permission_classes = [AllowAny]
    
    
    def  create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            self.perform_create(serializer)
            usuario = serializer.instance
            
            passwordGenerado = generar_password()
            usuario.set_password(passwordGenerado)
            usuario.save()
            
            asunto = "¡Bienvenido/a al Aplicativo de Eco_Denuncias!"
            mensajeCorreo = mensajeCorreo=f""" 
            Cordial saludo Usuario <b>{usuario.first_name} \
                {usuario.last_name}</b>, ¡Le damos la más cordial bienvenida!            
                <br><br>Le informamos que su cuenta para acceder al Aplicativo de Denuncias de Delitos Ambientales ha sido creada exitosamente. 
                <br>Agradecemos su compromiso con la protección de nuestros recursos naturales.
                A continuación, encontrará sus credenciales de acceso. 
                <br>Le recomendamos cambiar su contraseña la primera vez que ingrese al sistema por motivos de seguridad
                <br><br> \
                <b>Username:</b> {usuario.username}<br> 
                <b>Password:</b> {passwordGenerado}<br>
                <br>
                Puede acceder al aplicativo a través del siguiente enlace: https://www.Eco_Denucnias.com/es/mobile-app/
                <br><br> \
                Si tiene alguna dificultad para ingresar o necesita asistencia técnica, no dude en contactar a nuestro equipo de soporte en: 
                <br> 
                ecoddenuncias25@gmail.com o al teléfono 320-111-1111.

                """
            thread = threading.Thread(
                target=enviarCorreo, args=(asunto, mensajeCorreo, [usuario.email],None)
            )    
            thread.start()
            
            return Response(
                {
                    'mensaje': 'Usuario fue creado correctamente', 'data': serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {
                    'mensaje': 'Error al guardar el usuario', 'errores': serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )
            
        
class UsuariosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer
    

#
    
class RolesList(generics.ListCreateAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer

class RolesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer
 
#
    
class UsuarioRolesList(generics.ListCreateAPIView):
    queryset = UsuarioRoles.objects.all()
    serializer_class = UsuarioRolesSerializer

class UsuarioRolesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UsuarioRoles.objects.all()
    serializer_class = UsuarioRolesSerializer

#

class TerritorialesList(generics.ListCreateAPIView):
    queryset = Territoriales.objects.all()
    serializer_class = TerritorialesSerializer

class TerritorialesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Territoriales.objects.all()
    serializer_class = TerritorialesSerializer

#

class MunicipiosList(generics.ListCreateAPIView):
    queryset = Municipios.objects.all()
    serializer_class = MunicipiosSerializer


class MunicipiosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Municipios.objects.all()
    serializer_class = MunicipiosSerializer

#

class DependenciasList(generics.ListCreateAPIView):
    queryset = Dependencias.objects.all()
    serializer_class = DependenciasSerializer

class DependenciasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dependencias.objects.all()
    serializer_class = DependenciasSerializer

#
class FuncionariosList(generics.ListCreateAPIView):
    queryset = Funcionarios.objects.all()
    serializer_class = FuncionariosSerializer

class FuncionariosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Funcionarios.objects.all()
    serializer_class = FuncionariosSerializer
    
#

class RequerimientosList(generics.ListCreateAPIView):
    queryset = Requerimientos.objects.all()
    serializer_class = RequerimientosSerializer
    

class RequerimientosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Requerimientos.objects.all()
    serializer_class = RequerimientosSerializer
    
#

class DenunciasList(generics.ListCreateAPIView):
    queryset = Denuncias.objects.all()
    serializer_class = DenunciasSerializer

class DenunciasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Denuncias.objects.all()
    serializer_class = DenunciasSerializer

#

class SolicitudesList(generics.ListCreateAPIView):
    queryset = Solicitudes.objects.all()
    serializer_class = SolicitudesSerializer

class SolicitudesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Solicitudes.objects.all()
    serializer_class = SolicitudesSerializer
    
#
class RespuestasList(generics.ListCreateAPIView):
    queryset = Respuestas.objects.all()
    serializer_class = RespuestasSerializer
    
class RespuestasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Respuestas.objects.all()
    serializer_class = RespuestasSerializer

#
class SeguimientosList(generics.ListCreateAPIView):
    queryset = Seguimientos.objects.all()
    serializer_class = SeguimientosSerializer
    
class SeguimientosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seguimientos.objects.all()
    serializer_class = SeguimientosSerializer
    
#

class MultimediasList(generics.ListCreateAPIView):
    queryset = Multimedias.objects.all()
    serializer_class = MultimediasSerializer
    
class MultimediasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Multimedias.objects.all()
    serializer_class = MultimediasSerializer