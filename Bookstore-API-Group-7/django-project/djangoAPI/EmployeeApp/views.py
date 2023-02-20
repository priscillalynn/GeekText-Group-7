from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Departments, Employees
from EmployeeApp.serializers import DepartmentSeralizer, EmployeeSeralizer

# Create your views here. [API methods]

@csrf_exempt
def departmentApi(request, id=0):
    if request.method == 'GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSeralizer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)
    elif request.method == 'POST':
        departments_data = JSONParser().parse(request)
        departments_serializer = DepartmentSeralizer(data=departments_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        departments_data = JSONParser.parse(request)
        departments = Departments.objects.get(DepartmentId = departments_data['DepartmentId'])
        departments_serializer = DepartmentSeralizer(departments, data=departments_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        departments = Departments.objects.get(DepartmentId = id)
        departments.delete()
        return JsonResponse("Deleted Successfully", safe=False)