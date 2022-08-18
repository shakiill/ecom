from django.urls import path

from apps.frontend import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('shop/', views.ShopView.as_view(), name='shop'),
    path('product/<int:pk>/details/', views.ProductView.as_view(), name='product_details'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]
