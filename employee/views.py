from django.shortcuts import render
from .models import Employee, Student
from rest_framework import viewsets
from employee.serializers import EmployeeSerializers, StudnetSerializers
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics



# Create your views here.


def employee(request):
    user = Employee.objects.all()
    print(user)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers

# function based api
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


# class based api
class StudentAPI(APIView):
    def get(self, request):
        student = Student.objects.all()
        serializer = StudnetSerializers(student, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        data = request.data
        serializer = StudnetSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=401)


class Student_Details(APIView):
    def get_object(self, id):
        try:
            return Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response(status=404)

    def get(self, request, id):
        instance = self.get_object(id=id)
        serializer = StudnetSerializers(instance)
        return Response(serializer.data, status=200)

    def put(self, request, id=None, format=None):
        instance = self.get_object(id)
        serializer = StudnetSerializers(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id):
        instance = self.get_object(id)
        instance.delete()
        return Response(status=204)



class ApiGeneric(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    serializer_class=StudnetSerializers
    queryset=Student.objects.all()

    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)