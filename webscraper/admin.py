
from django.contrib import admin
from .models import SanctionedEntity, ServidorPublico, EmpresaNoAutorizada

@admin.register(SanctionedEntity)
class SanctionedEntityAdmin(admin.ModelAdmin):
    list_display = ('title', 'entity', 'country', 'from_date', 'to_date')
    search_fields = ('entity', 'country', 'title')

@admin.register(ServidorPublico)
class ServidorPublicoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cargo', 'entidad', 'nivel', 'estado', 'departamento')
    search_fields = ('nombre', 'entidad', 'departamento')


@admin.register(EmpresaNoAutorizada)
class EmpresaNoAutorizadaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'razon', 'fecha')
    search_fields = ('nombre', 'direccion')
