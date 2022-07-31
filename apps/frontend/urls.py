from django.urls import path

from apps.frontend import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('shop/', views.ShopView.as_view(), name='shop'),
    path('contact/', views.ShopView.as_view(), name='contact'),
]
