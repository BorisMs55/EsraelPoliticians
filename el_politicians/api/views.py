import datetime
import json
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from rest_framework import viewsets
from employee.models import Employee
from rest_framework.renderers import JSONRenderer

from .serializers import EmployeeSerializer
from rest_framework import serializers


# Create your views here.

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


def salaryCalc(request):
    employee_obj = EmployeeSerializer.data
    # print("salaryCalc")
    employee = Employee.objects.all()
    serializer = EmployeeSerializer(employee, many=True)
    json_data = JSONRenderer().render(serializer.data)

    list_data = json.loads(json_data)
    record_count=len(list_data)
    salary_sum = 0.0
    now = datetime.datetime.now()

    for item in list_data:
        salary_sum = salary_sum + float(item.get('salary'))
        #print(item.get('hire_date'), item.get('salary'))
    #print(salary_sum)
    salary_avg = salary_sum / record_count
    #print(salary_avg)

    list_out = []
    for item in list_data:
        adate = datetime.datetime.fromisoformat(item.get('hire_date'))

        delta = (now - adate).days
        if (delta < 365) and (float(item.get('salary')) < salary_avg):
            list_out.append(item)
    #print(list_out)
    with open("result.txt", 'w') as file:
        file.write("average salary="+str(salary_avg)+"\n")
        for row in list_out:
            #s = " ".join(map(str, row))
            s = str(row)
            file.write(s + '\n')

    return redirect('/')
