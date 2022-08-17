from django.db import models


# Create your models here.
class HomeSlider(models.Model):
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=255)
    image = models.ImageField(upload_to='slider')
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title
