from django.shortcuts import render
from .models import Employee
from rest_framework import viewsets
from employee.serializers import EmployeeSerializers

# Create your views here.
def employee(request):
    user=Employee.objects.all()
    print(user)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializers