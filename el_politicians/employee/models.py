from django.db import models
from djmoney.models.fields import MoneyField
from django_extensions.db.fields import AutoSlugField

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    email = models.EmailField()
    phone_number = models.CharField(max_length=16)
    hire_date = models.DateField()
    salary = MoneyField(max_digits=14, decimal_places=2, default_currency='ILS')
    commission_pct = models.DecimalField(max_digits=4, decimal_places=2)
    manager = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    photo = models.ImageField(default='default.png', blank=True)
    job = models.ForeignKey('Job', null=True, on_delete=models.SET_NULL)
    department = models.ForeignKey('Department', null=True, blank=True, on_delete=models.SET_NULL)
    slug = AutoSlugField(populate_from=['first_name', 'last_name'])

    def slugify_function(self, content):
        return content.replace('_', '-').lower()

    def __str__(self):
        return self.first_name + " " + self.last_name


class Job(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
