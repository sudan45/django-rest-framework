from . import views
from django.urls import path,include
from employee import function_views
from rest_framework.routers import DefaultRouter
from employee.views import Studentviewset


router=DefaultRouter()
router.register('student',views.Studentviewset,basename='student')


urlpatterns = [
    path('employeelist',views.employee ,name='employee'),
    path('studentlist/',function_views.student,name='student'),
    path('viewset/',include(router.urls))
    
    

 ]

