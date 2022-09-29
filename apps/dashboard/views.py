from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class DashboardView(TemplateView):
    template_name = 'admin/home.html'


class BillView(TemplateView):
    template_name = 'admin/bill.html'


class OrderView(TemplateView):
    template_name = 'admin/order.html'
