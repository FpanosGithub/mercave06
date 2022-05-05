from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CrearUsuarioForm(UserCreationForm):
    class Meta:
        model= get_user_model()
        fields = ('username', 'email', 'organizacion')

class ModificarUsuarioForm(UserChangeForm):
    class Meta:
        model= get_user_model()
        fields = ('username', 'email', 'organizacion')