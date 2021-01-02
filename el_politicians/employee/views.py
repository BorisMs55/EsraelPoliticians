from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *

# Create your views here.

class EmployeeListView(APIView):
    """Employee List"""

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'employee/employee_list.html'

    def get(self, request):
        queryset = Employee.objects.all()
        return Response({'employees': queryset})
