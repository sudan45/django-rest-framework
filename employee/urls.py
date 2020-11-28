from . import views
from django.urls import path,include
from employee import function_views
from rest_framework.routers import DefaultRouter
from employee.views import Studentviewset,StudentModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView


router=DefaultRouter()
router.register('student',views.Studentviewset,basename='student')
router.register('studentmodel',views.StudentModelViewSet,basename='modelviewset')


urlpatterns = [
    path('employeelist',views.employee ,name='employee'),
    path('studentlist/',function_views.student,name='student'),
    path('viewset/',include(router.urls)),
    path('gettoken/',TokenObtainPairView.as_view(),name='gettoken'),
    path('refreshtoken/',TokenRefreshView.as_view(),name='refreshtoken'),
    path('verifytoken/',TokenVerifyView.as_view(),name='verifytoken'),



 ]

