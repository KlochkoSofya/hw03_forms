from django.shortcuts import render
from django.views.generic import CreateView

from django.urls import reverse_lazy

#  импортируем класс формы, чтобы сослаться на неё во view-классе
from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("signup") #  где signup — это параметр "name" в path()
    template_name = "posts/signup.html" 