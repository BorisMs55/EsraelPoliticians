from django.urls import path
from .views import *

app_name = 'employee'

urlpatterns = [
    path('list/', EmployeeListView.as_view(), name='list'),
    # path('<int:pk>/', views.EmployeeDetailView.as_view()),
]