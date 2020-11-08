from . import views
from django.urls import path,include
from rest_framework import routers
from employee.views import *

router = routers.DefaultRouter()
router.register('', EmployeeViewSet)

urlpatterns = [
    path('employee/',include(router.urls)),
    path('student/',student),
    path('student/<id>/',student_details),
    path('studnetcb/',StudentAPI.as_view()),
    path('studnetcb/<int:id>/',Student_Details.as_view()),
    path('genericapi',ApiGeneric.as_view())
]

