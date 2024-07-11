from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import FormView

from users.forms import UserForm

from users.models import Profile


class LoginView(FormView):
    form_class = UserForm
    success_url = '/home'
    template_name = 'users/login.html'
    model = User

    def form_valid(self, form):
        response = super().form_valid(form)
        data = form.cleaned_data
        Profile.objects.create(username=data['username'])
        return response

