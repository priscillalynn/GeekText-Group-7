from rest_framework import serializers
from .models import Department, Employees

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('department_id', 'department_name', 'employee_count', 'manager')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('employee_id', 'name', 'email', 'phone_number', 'job_title', 'department', 'joining_date')