from rest_framework import serializers
from employee.models import Employee,Student


class EmployeeSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'first_name',
            'last_name',
            'phone',
            'email',
            'url'
        )


class StudnetSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            'id',
            'first_name',
            'last_name',
            'phone',
            'email',
        )