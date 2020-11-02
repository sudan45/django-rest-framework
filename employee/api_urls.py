from . import views
from django.urls import path,include
from rest_framework import routers
from employee.views import *

router = routers.DefaultRouter()
router.register('', EmployeeViewSet)

urlpatterns = [
    path('employee/',include(router.urls)),
    path('student/',student),
    path('student/<int:id>',student_details)


 ]

