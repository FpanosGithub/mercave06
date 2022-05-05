from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CrearUsuarioForm, ModificarUsuarioForm
from .models import Usuario

# Register your models here.

class UsuarioAdmin(UserAdmin):
    add_form = CrearUsuarioForm
    form = ModificarUsuarioForm
    model = Usuario
    list_display = ['email','username', 'organizacion', 'is_staff']
    fieldsets = UserAdmin.fieldsets + ((None, {"fields":("organizacion",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields":("organizacion",)}),)

admin.site.register(Usuario, UsuarioAdmin)