from django.urls import path, include
from .views import EmployeeViewset
from . import views

app_name = 'api'

urlpatterns = [
    path('', EmployeeViewset.as_view({'get': 'list', }), name="display_json"),
    path('actionUrl/', views.salaryCalc, name="salaryCalc"),
]
