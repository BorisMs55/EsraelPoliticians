from django.shortcuts import render, redirect
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


# Create your views here.

class EmployeeListView(APIView):
    """Employee List"""

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'employee/employee_list.html'

    def get(self, request):
        queryset = Employee.objects.all()
        return Response({'employees': queryset})


@login_required(login_url="/accounts/login/")
def employee_create(request):
    if request.method == 'POST':
        form = CreateEmployee(request.POST, request.FILES)
        if form.is_valid():
            # save to DB
            form.save()
            return redirect('employee:list')
    else:
        form = CreateEmployee()
    return render(request, 'employee/employee_create.html', {'form': form})


@login_required(login_url="/accounts/login/")
def department_create(request):
    if request.method == 'POST':
        form = CreateDepartment(request.POST, request.FILES)
        if form.is_valid():
            # save to DB
            form.save()
            return redirect('employee:list')
    else:
        form = CreateDepartment()
    return render(request, 'employee/department_create.html', {'form': form})


@login_required(login_url="/accounts/login/")
def job_create(request):
    if request.method == 'POST':
        form = CreateJob(request.POST, request.FILES)
        if form.is_valid():
            # save to DB
            form.save()
            return redirect('employee:list')
    else:
        form = CreateJob()
    return render(request, 'employee/job_create.html', {'form': form})
