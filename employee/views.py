from django.shortcuts import render
from .models import Employee, Student
from rest_framework import viewsets
from employee.serializers import EmployeeSerializers, StudnetSerializers
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


def employee(request):
    user = Employee.objects.all()
    print(user)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers


@csrf_exempt
def student(request):
    if request.method == 'GET':
        student = Student.objects.all()
        serializer = StudnetSerializers(student, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StudnetSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=401)


@csrf_exempt
def student_details(request, id):
    try:
        instance = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return HttpResponse(Status=404)

    if request.method == 'GET':
        student = Student.objects.all()
        serializer = StudnetSerializers(student, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StudnetSerializers(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        instance.delete()
        return HttpResponse(status=204)
