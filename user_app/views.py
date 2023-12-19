from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import forms
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.views.generic import CreateView, RedirectView
from django.contrib.auth import authenticate, logout


class SignUpView(CreateView):
    model = User
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
    form_class = forms.UserSignUpForm
    success_message = "Your profile was created successfully"


class UserLogin(LoginView):
    template_name = 'login.html'
    model = User

    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successful')
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy("home")

    def form_invalid(self, form):
        messages.success(self.request, 'Logged in information is not correct')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class LogoutUser(RedirectView):

    url = '/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutUser, self).get(request, *args, **kwargs)
