from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from apps.account.forms import CustomerRegForm
from apps.account.models import Customer


class RegisterView(CreateView):
    model = Customer
    form_class = CustomerRegForm
    success_url = reverse_lazy('home')
    template_name = 'register.html'
