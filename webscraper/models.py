from django.db import models


class SanctionedEntity(models.Model):
    title = models.CharField(max_length=255)
    entity = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    from_date = models.CharField(max_length=100)
    to_date = models.CharField(max_length=100)
    prohibited_practice = models.TextField()
    source = models.CharField(max_length=255)
    idb_sanction_type = models.CharField(max_length=255)
    idb_sanction_source = models.CharField(max_length=255)
    other_name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.entity

class EnvironmentalSanction(models.Model):
    entidad = models.CharField("Entidad", max_length=255)
    tipo_documento = models.CharField("Tipo de Documento", max_length=100)
    numero_documento = models.CharField("Número de Documento", max_length=100, unique=True)
    nombre_infractor = models.CharField("Nombre del Infractor", max_length=255)
    autoridad = models.CharField("Autoridad Ambiental", max_length=255)
    acto = models.CharField("Acto Administrativo", max_length=255)
    fecha_acto = models.CharField("Fecha del Acto", max_length=100)
    estado = models.CharField("Estado", max_length=100)

    def __str__(self):
        return f"{self.nombre_infractor} - {self.numero_documento}"


class ServidorPublico(models.Model):
    nombre = models.CharField(max_length=255)
    cargo = models.CharField(max_length=255)
    entidad = models.CharField(max_length=255)
    nivel = models.CharField(max_length=100, default="No definido")
    estado = models.CharField(max_length=100, default="Desconocido")
    departamento = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
    from django.db import models

class EmpresaNoAutorizada(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.TextField(blank=True, null=True)
    razon = models.TextField(blank=True, null=True)
    fecha = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nombre


class Fugitive(models.Model):
    fecha_captura = models.DateField("Fecha de Captura")
    nombre = models.CharField("Nombre", max_length=255)
    cargos = models.TextField("Cargos", blank=True)
    raza = models.CharField("Raza", max_length=50, blank=True)
    sexo = models.CharField("Sexo", max_length=20, blank=True)
    estatura = models.CharField("Estatura", max_length=20, blank=True)
    peso = models.CharField("Peso", max_length=20, blank=True)
    color_cabello = models.CharField("Color de Cabello", max_length=50, blank=True)
    color_ojos = models.CharField("Color de Ojos", max_length=50, blank=True)
    ano_nacimiento = models.CharField("Año de Nacimiento", max_length=10, blank=True)
    ncic = models.CharField("NCIC #", max_length=50, blank=True)
    jurisdiccion = models.CharField("Jurisdicción", max_length=255, blank=True)
    notas = models.TextField("Notas", blank=True)
    url = models.URLField("URL de Perfil", unique=True, max_length=500)

    def __str__(self):
        return self.nombre
