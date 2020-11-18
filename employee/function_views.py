from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

def student(request):
    return HttpResponse("hi student")


