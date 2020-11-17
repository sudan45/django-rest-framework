from rest_framework import serializers
from employee.models import Employee, Student
from rest_framework import exceptions
from django.contrib.auth import authenticate


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


class LoginSerializers(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                data["user"] = user
            else:
                msg="unable to login"
                raise exceptions.ValidationError(msg)
        else:
            msg = "Username or Password are incorrect"
            raise exceptions.ValidationError(msg)
        return data
