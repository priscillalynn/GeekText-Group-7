from django.contrib import admin
from .models import Employees, Department

admin.site.register(Employees)
admin.site.register(Department)

class DepartmentAdmin(admin.ModelAdmin):
    fields = ['name', 'employee_count', 'manager']

class EmployeeAdmin(admin.ModelAdmin):
    fields = ('name', 'email', 'phone_number', 'job_title', 'department', 'joining_date')