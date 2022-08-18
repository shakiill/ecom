from django.db import models

# Create your models here.
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='category', null=True, blank=True)
    serial = models.IntegerField(unique=True, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, unique=True)

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cat_products')
    color = models.ManyToManyField(Color, related_name='color_product')
    size = models.ManyToManyField(Size, related_name='color_product')
    price = models.FloatField()
    photo = models.ImageField(upload_to='product')
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_stock = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            a = slugify(self.name)
            b = '-'
            cc = Product.objects.last().order_by('id')
            c = str(cc.id + 1)
            d = a + b + c
            self.slug = d
        return super().save(*args, **kwargs)


class ProductPhoto(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_image')
    photo = models.ImageField(upload_to='product')

    def __str__(self):
        return self.product.name
