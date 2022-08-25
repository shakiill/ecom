from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, DetailView, ListView

from apps.frontend.models import HomeSlider
from apps.product.models import Category, Product, ProductPhoto, Color


class HomeView(TemplateView):
    template_name = "frontend/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slider_list'] = HomeSlider.objects.all()
        context['cat_list'] = Category.objects.all()
        context['featured'] = Product.objects.filter(is_featured=True, is_active=True)
        context['latest'] = Product.objects.filter(is_active=True).order_by('-id')[0:8]
        return context


class ShopView(ListView):
    model = Product
    template_name = "frontend/shop.html"

    queryset = Product.objects.all()

    def get_queryset(self):
        qs = super(ShopView, self).get_queryset()
        lr = self.request.GET.get('lower', None)
        up = self.request.GET.get('upper', None)
        cat = self.request.GET.get('cat', None)
        color = self.request.GET.get('color', None)
        if color:
            qs = qs.filter(color=color)
        if cat:
            qs = qs.filter(category=cat)
        if lr:
            qs = qs.filter(price__gte=lr)
        if up:
            qs = qs.filter(price__lte=up)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_list'] = Category.objects.all()
        context['color_list'] = Color.objects.all()
        return context


class ProductView(DetailView):
    model = Product
    template_name = 'frontend/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['img_list'] = ProductPhoto.objects.filter(product=self.object.pk)
        return context


class ContactView(TemplateView):
    template_name = "frontend/contact.html"
