from django.contrib import messages
from django.shortcuts import render,redirect
import string
import random
# para correo
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from smtplib import SMTPException
from .models import *
from django.db import Error, transaction
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import authenticate, login , logout
from .forms import LoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth
# Create your views here.




def enviarCorreo(asunto=None, mensaje=None, destinatario=None, archivo=None):
    remitente = settings.EMAIL_HOST_USER
    template = get_template('enviarCorreo.html')
    contenido = template.render({'mensaje': mensaje})
    try:
        correo = EmailMultiAlternatives(
            asunto, mensaje, remitente, destinatario)
        correo.attach_alternative(contenido, 'text/html')
        if archivo != None:
            correo.attach_file(archivo)
        correo.send(fail_silently=False)
    except SMTPException as error:
        print(error)
        
        

def generar_password(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longitud))



def login_view(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            # 🔸 Bloquear staff o superusuarios
            if user.is_staff or user.is_superuser:
                return render(request, 'login.html', {
                    'form': form,
                    'error': 'Acceso restringido para este tipo de usuario.'
                })
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {
                'form': form,
                'error': 'Usuario o contraseña incorrectos.'
            })
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})





@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')



@login_required
def dashboard_view(request):
    tipo_de_rol = UsuarioRoles.objects.filter(usuario=request.user)
    
    permissions = {
        'admin',
        'funcionario',
        'usuario'
    }
    
    context ={
        'usuario': request.user,
        'permissions': permissions,
        'roles': [rol.rol.nombre_rol for rol in tipo_de_rol]
    }

    return render(request, 'home.html', context)





def territoriales(request):
    if request.method == 'POST':
        nombreTerritorial = request.POST.get('nombre_territorial')
        
        territorial = Territoriales.objects.create(nombre_territorial=nombreTerritorial)
        
        territorial.save()
        
        return JsonResponse({'mensaje': 'Territorial creado exitosamente', 'nombre_territorial': nombreTerritorial})
    return JsonResponse({'mensaje': 'Método no permitido'}, status=405)
        
