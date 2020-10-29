from rest_framework import serializers
from employee.models import Employee


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
