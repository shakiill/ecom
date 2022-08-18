from django.contrib import admin

# Register your models here.
from django.contrib.admin import TabularInline

from apps.product.models import Category, Size, Color, Product, ProductPhoto


class PhotoInline(TabularInline):
    model = ProductPhoto
    fields = ['photo', ]
    show_change_link = True
    extra = 0
    fk_name = "product"


class ProductAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, ]
    model = Product
    list_display = ['name', 'category', 'price', 'is_featured', 'is_active']
    # list_filter = ['order__order__buyer', 'status', 'is_received']


admin.site.register(Category)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductPhoto)
