from re import template
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CrearUsuarioForm

class SignUpView(CreateView):
    form_class= CrearUsuarioForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"
