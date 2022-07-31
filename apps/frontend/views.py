from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "frontend/home.html"


class ShopView(TemplateView):
    template_name = "frontend/shop.html"


class ContactView(TemplateView):
    template_name = "frontend/contact.html"
