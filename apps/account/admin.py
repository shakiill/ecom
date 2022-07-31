from django.contrib import admin
from .models import Staff, Customer, CustomUser, Profile


# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['username', 'name', 'gender']
    fields = ['username', 'name', 'photo', 'gender', 'password']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['customer', 'contact']


admin.site.register(Staff)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(CustomUser)
