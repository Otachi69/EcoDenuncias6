from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


tipo_de_rol = [
    ('usuario', 'usuario'),
    ('admin', 'admin'),
    ('funcionario', 'funcionario'),
]
estado_usuario_rol = [
    ('activo', 'activo'),
    ('inactivo', 'inactivo'),
]


Municipio = [
('Almaguer', 'Almaguer'),
('Argelia', 'Argelia'),
('Balboa', 'Balboa'),
('Bolívar', 'Bolívar'),
('Buenos Aires', 'Buenos Aires'),
('Cajibío', 'Cajibío'),
('Caldono', 'Caldono'),
('Caloto', 'Caloto'),
('Corinto', 'Corinto'),
('El Tambo', 'El Tambo'),
('Florencia', 'Florencia'),
('Guachené', 'Guachené'),
('Guapi', 'Guapi'),
('Inzá', 'Inzá'),
('Jambaló', 'Jambaló'),
('La Sierra', 'La Sierra'),
('La Vega', 'La Vega'),
('López de Micay', 'López de Micay'),
('Mercaderes', 'Mercaderes'),
('Miranda', 'Miranda'),
('Morales', 'Morales'),
('Padilla', 'Padilla'),
('Páez', 'Páez'),
('Patía', 'Patía'),
('Piamonte', 'Piamonte'),
('Piendamó', 'Piendamó'),
('Popayán', 'Popayán'),
('Puerto Tejada', 'Puerto Tejada'),
('Puracé', 'Puracé'),
('Rosas', 'Rosas'),
('San Sebastián', 'San Sebastián'),
('Santander de Quilichao', 'Santander de Quilichao'),
('Santa Rosa', 'Santa Rosa'),
('Silvia', 'Silvia'),
('Sotará', 'Sotará'),
('Suárez', 'Suárez'),
('Sucre', 'Sucre'),
('Timbío', 'Timbío'),
('Timbiquí', 'Timbiquí'),
('Toribío', 'Toribío'),
('Totoró', 'Totoró'),
('Villa Rica', 'Villa Rica'),
]

tipo_requerimiento = [
    ('denuncia', 'denuncia'),
    ('solicitud', 'solicitud'),
]

estado_requerimiento = [
    ('pendiente', 'pendiente'),
    ('en_proceso', 'en_proceso'),
    ('resuelto', 'resuelto'),
]

nombre_delito = [
('Aprovechamiento ilícito de los recursos naturales renovables', 'Aprovechamiento ilícito de los recursos naturales renovables'),
('Tráfico de fauna', 'Tráfico de fauna'),
('Caza ilegal', 'Caza ilegal'),
('Pesca ilegal', 'Pesca ilegal'),
('Manejo ilícito de especies exóticas', 'Manejo ilícito de especies exóticas'),
('Deforestación', 'Deforestación'),
('Promoción y financiación de la deforestación', 'Promoción y financiación de la deforestación'),
('Manejo y uso ilícito de organismos genéticamente modificados, microorganismos y sustancias o elementos peligrosos', 'Manejo y uso ilícito de organismos genéticamente modificados, microorganismos y sustancias o elementos peligrosos'),
('Explotación ilícita de yacimiento minero y otros materiales', 'Explotación ilícita de yacimiento minero y otros materiales'),
('Contaminación ambiental', 'Contaminación ambiental'),
('Impacto ambiental grave', 'Impacto ambiental grave'),
('Daños en los recursos naturales y ecocidio', 'Daños en los recursos naturales y ecocidio'),
('Invasión de Áreas de Especial Importancia Ecológica (AEIE)', 'Invasión de Áreas de Especial Importancia Ecológica (AEIE)'),
('Financiación de invasión de Áreas de Especial Importancia Ecológica (AEIE)', 'Financiación de invasión de Áreas de Especial Importancia Ecológica (AEIE)'),

]

nombre_solicitud = [
('Solicitud de inspección ambiental', 'Solicitud de inspección ambiental'),
('Solicitud de seguimiento y control de vertimientos', 'Solicitud de seguimiento y control de vertimientos'),
('Solicitud de reparación integral del daño ambiental', 'Solicitud de reparación integral del daño ambiental'),
('Solicitud de remediación de suelos contaminados', 'Solicitud de remediación de suelos contaminados'),
('Solicitud de mitigación de fuentes contaminantes', 'Solicitud de mitigación de fuentes contaminantes'),
('Solicitud de suspensión de actividades mineras ilegales', 'Solicitud de suspensión de actividades mineras ilegales'),
('Solicitud de protección de fuentes de agua', 'Solicitud de protección de fuentes de agua'),
('Solicitud de reforestación en zona afectada', 'Solicitud de reforestación en zona afectada'),
('Solicitud de compensación ambiental', 'Solicitud de compensación ambiental'),
('Solicitud de transparecia e información sobre impacto ambiental', 'Solicitud de transparencia e información sobre impacto ambiental'),

]

tipo_multimedia = [
    ('imagen', 'imagen'),
    ('video', 'video'),
    ('archivo', 'archivo'),
]


class Usuarios(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=200, unique=True)
    identificacion = models.CharField(max_length=12, unique=True)
    telefono = models.CharField(max_length=15, unique=True)
    
    def __str__(self):
        return self.username
    
class Roles(models.Model):
    nombre_rol =  models.CharField( null= False, choices= tipo_de_rol, unique=True)

    def __str__(self):
        return self.nombre_rol


class UsuarioRoles(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    rol = models.ForeignKey(Roles, on_delete=models.CASCADE)
    estado_usuario_rol = models.CharField(choices= estado_usuario_rol, default='activo', max_length=10)

    def __str__(self):
        return f"{self.usuario.username} - {self.rol.nombre_rol}"

    
class Territoriales(models.Model):
    nombre_territorial = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre_territorial
    
class Municipios(models.Model):
    nombre_municipio = models.CharField(choices= Municipio, max_length=100, unique=True)
    territorial= models.ForeignKey(Territoriales, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_municipio
    
class Dependencias(models.Model):
    nombre_dependencia = models.CharField(max_length=100, unique=True)
    territorial = models.ForeignKey(Territoriales, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_dependencia

class Funcionarios(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    dependencia = models.ForeignKey(Dependencias, on_delete=models.CASCADE)
    es_jefe = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.usuario.username} - {self.dependencia.nombre_dependencia}"


class Requerimientos(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    tipo_requerimiento = models.CharField(max_length=50, choices= tipo_requerimiento, unique=True)
    estado = models.CharField(max_length=20, choices= estado_requerimiento, default='pendiente')
    radicado = models.CharField(max_length=10, unique=True)
    
    def __str__(self):
        return f"{self.tipo_requerimiento} - {self.radicado}"



class Denuncias(models.Model):
    requerimiento = models.ForeignKey(Requerimientos, on_delete=models.CASCADE)
    nombre_delito = models.CharField(choices= nombre_delito)
    descripcion_delito = models.TextField()
    fecha_delito = models.DateField()
    municipio = models.ForeignKey(Municipios, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nombre_delito} - {self.requerimiento.radicado}"


class Solicitudes(models.Model):
    requerimiento = models.ForeignKey(Requerimientos, on_delete=models.CASCADE)
    nombre_solicitud = models.CharField(choices=nombre_solicitud)
    descripcion_solicitud = models.TextField()
    fecha_solicitud = models.DateField()
    municipio = models.ForeignKey(Municipios, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.descripcion_solicitud} - {self.requerimiento.radicado}"

    

class Seguimientos(models.Model):
    requerimiento = models.ForeignKey(Requerimientos, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionarios, on_delete=models.CASCADE)
    fecha_seguimiento = models.DateField()
    actualizacion_reciente = models.DateTimeField(auto_now=True)
    dias_abierta = models.IntegerField()
    descripcion_actualizacion = models.TextField()
    tiempo_limite = models.DateField()
    
    def __str__(self):
        return f"{self.requerimiento.radicado} - {self.funcionario.usuario.username} - {self.fecha_seguimiento}"

    
class Respuestas(models.Model):
    fecha_respuesta = models.DateField(auto_now_add=True)
    descripcion_respuesta = models.TextField()
    seguimiento = models.ForeignKey(Seguimientos, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f"{self.fecha_respuesta} - {self.descripcion_respuesta} - {self.seguimiento}"
    

class Multimedias(models.Model):
    requerimiento = models.ForeignKey(Requerimientos, on_delete=models.CASCADE)
    respuesta = models.ForeignKey(Respuestas, on_delete=models.CASCADE, null=True, blank=True)
    multimedia = models.CharField(choices= tipo_multimedia)
    nombre_archivo = models.FileField(upload_to='multimedias/')
    
    
    def __str__(self):
        return f"{self.nombre_archivo} - {self.requerimiento.radicado}"