from django.urls import path

from apps.account import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='customer_reg'),
]
