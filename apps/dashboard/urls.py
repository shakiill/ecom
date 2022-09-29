from django.urls import path

from apps.dashboard import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('bill/', views.BillView.as_view(), name='bill'),
    path('order/', views.OrderView.as_view(), name='order'),
]
