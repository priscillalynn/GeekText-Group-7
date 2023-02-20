from rest_framework import serializers
from EmployeeApp.models import Departments, Employees

class DepartmentSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('DepartmentId', 'DepartmentName')

class EmployeeSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('EmployeeId', 'EmployeeName', 'Department', 'DateOfJoining', 'PhotoFileName')