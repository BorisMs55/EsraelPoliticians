from django.urls import path
from .views import *

app_name = 'employee'

urlpatterns = [
    path('list/', EmployeeListView.as_view(), name='list'),
    path('em_create/', employee_create, name='employee_create'),
    path('dp_create/', department_create, name='department_create'),
    path('jb_create/', job_create, name='job_create'),
]