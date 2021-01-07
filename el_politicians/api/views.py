import datetime
import json

import requests
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
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
    # employee = Employee.objects.all()
    # serializer = EmployeeSerializer(employee, many=True)
    # json_data = JSONRenderer().render(serializer.data)

    # json_data = response.json()
    # list_data = json.loads(json_data)
    # record_count=len(list_data)
    url1 = reverse('api:display_json')
    #print(url1)
    response = requests.get("http://127.0.0.1:8000"+url1)

    # url = 'http://127.0.0.1:8000/api/'
    # response = requests.get(url)
    data = json.loads(response.text.encode("utf8"))
    # print(data)
    record_count = len(data)
    #print(record_count)
    salary_sum = 0.0
    now = datetime.datetime.now()

    for item in data:
        #print(float(item.get('salary')))
        salary_sum = salary_sum + float(item.get('salary'))
    #print(salary_sum)
    salary_avg = salary_sum / record_count
    #print(salary_avg)

    list_out = []
    for item in data: #list_data:
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
