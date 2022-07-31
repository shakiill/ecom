from django.contrib.auth.models import AbstractUser, Group
from django.db import models

# Create your models here.
from django.db.models import SET_NULL
from django.utils.crypto import get_random_string

from apps.account.manager import StaffManager, CustomerManager
from apps.location.models import Country, Division, District


class CustomUser(AbstractUser):
    username = models.CharField(unique=True, max_length=60)

    class GenderChoices(models.IntegerChoices):
        MALE = 1, 'Male'
        FEMALE = 2, 'Female'
        OTHERS = 3, 'Others'

    last_name = None
    first_name = None
    name = models.CharField(verbose_name='Full Name', max_length=60)
    photo = models.ImageField(upload_to='users', null=True, blank=True)
    gender = models.SmallIntegerField(choices=GenderChoices.choices, default=1)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Staff(CustomUser):
    class Meta:
        proxy = True

    objects = StaffManager()

    def save(self, *args, **kwargs):
        self.is_staff = True
        # password = get_random_string(length=6, allowed_chars='ABCD0123456789')
        # print(password)
        # self.set_password(password)
        super(Staff, self).save(*args, **kwargs)
        # send sms script


class Customer(CustomUser):
    class Meta:
        proxy = True

    objects = CustomerManager()

    def save(self, *args, **kwargs):
        super(Customer, self).save(*args, **kwargs)
        group, created = Group.objects.get_or_create(name='customer')
        self.groups.set([group])


class Profile(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    contact = models.CharField(max_length=20, verbose_name='Phone number')
    dob = models.DateField(verbose_name='Date Of Birth')
    country = models.ForeignKey(Country, on_delete=SET_NULL, null=True, blank=True, related_name='country_customer')
    division = models.ForeignKey(Division, on_delete=SET_NULL, null=True, blank=True, related_name='div_customer')
    district = models.ForeignKey(District, on_delete=SET_NULL, null=True, blank=True, related_name='dict_customer')
    address = models.TextField()

    def __str__(self):
        return self.customer.name
