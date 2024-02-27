from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from users.forms import CustomAuthenticationForm, CustomUserCreationForm


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = CustomAuthenticationForm
    success_url = reverse_lazy('home')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')


class SignUpView(CreateView):
    template_name = 'users/signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
