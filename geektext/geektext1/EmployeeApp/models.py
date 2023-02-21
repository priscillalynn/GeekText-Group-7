from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    employee_count = models.IntegerField(default=0)
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class Employees(models.Model):
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='John Doe')
    email = models.EmailField(default='abc123@mail.com')
    phone_number = models.CharField(max_length=15)
    job_title = models.CharField(max_length=100)
    department = models.CharField(max_length=100, default='default_department')
    joining_date = models.DateField(default='timezone.now')

    def __str__(self):
        return self.name