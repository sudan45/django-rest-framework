from . import views
from django.urls import path


urlpatterns = [
    path('employeelist',views.employee ,name='employee')

 ]

