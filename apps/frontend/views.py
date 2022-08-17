from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from apps.frontend.models import HomeSlider
from apps.product.models import Category


class HomeView(TemplateView):
    template_name = "frontend/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slider_list'] = HomeSlider.objects.all()
        context['cat_list'] = Category.objects.all()
        return context


class ShopView(TemplateView):
    template_name = "frontend/shop.html"


class ContactView(TemplateView):
    template_name = "frontend/contact.html"
