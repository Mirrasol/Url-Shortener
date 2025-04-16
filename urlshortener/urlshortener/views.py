# from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView


class Homepage(TemplateView):
    template_name = 'homepage.html'


class CustomLoginView(SuccessMessageMixin, LoginView):
    """
    Add a custom message for a successful user login.
    """
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_message = 'You are logged in'


class CustomLogoutView(LogoutView):
    """
    Add a custom message for a successful user logout.
    """
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, 'You are logged out')
        return super().dispatch(request, *args, **kwargs)


class CustomUserCreateView(SuccessMessageMixin, CreateView):
    """
    Create a new user, with a custom success message.
    """
    template_name = 'sign_up.html'
    model = get_user_model()
    form_class = UserCreationForm
    success_message = 'Registration Successful!'
    success_url = reverse_lazy('login')
