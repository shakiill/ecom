from django.contrib import admin

# Register your models here.
from apps.location.models import Country, Division, District

admin.site.register(Country)
admin.site.register(Division)
admin.site.register(District)
