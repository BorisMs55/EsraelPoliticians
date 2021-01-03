from django import forms
from . import models


class CreateEmployee(forms.ModelForm):
    class Meta:
        model = models.Employee
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'hire_date', 'salary', 'commission_pct',
                  'manager', 'photo', 'job', 'department']

class CreateDepartment(forms.ModelForm):
    class Meta:
        model = models.Department
        fields = ['name']
