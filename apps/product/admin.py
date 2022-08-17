from django.contrib import admin

# Register your models here.
from apps.product.models import Category, Size, Color, Product, ProductPhoto

admin.site.register(Category)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Product)
admin.site.register(ProductPhoto)
