from django import forms
from django_select2 import forms as s2forms
from . import models

class JobWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "name__icontains",
    ]

class CreateEmployee(forms.ModelForm):
    class Meta:
        model = models.Employee
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'hire_date', 'salary', 'commission_pct',
                  'manager', 'photo', 'job', 'department']
        # widgets = {
        #     "job": JobWidget,
        # }

class CreateDepartment(forms.ModelForm):
    class Meta:
        model = models.Department
        fields = ['name']

class CreateJob(forms.ModelForm):
    class Meta:
        model = models.Job
        fields = ['name']
