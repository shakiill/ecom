from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, DetailView

from apps.frontend.models import HomeSlider
from apps.product.models import Category, Product


class HomeView(TemplateView):
    template_name = "frontend/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slider_list'] = HomeSlider.objects.all()
        context['cat_list'] = Category.objects.all()
        context['featured'] = Product.objects.filter(is_featured=True, is_active=True)
        context['latest'] = Product.objects.filter(is_active=True).order_by('-id')[0:8]
        return context


class ShopView(TemplateView):
    template_name = "frontend/shop.html"


class ProductView(DetailView):
    model = Product
    template_name = 'frontend/product.html'


class ContactView(TemplateView):
    template_name = "frontend/contact.html"
