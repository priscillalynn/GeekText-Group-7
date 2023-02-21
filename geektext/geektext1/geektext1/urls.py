from django.contrib import admin
from django.urls import path
from EmployeeApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('departments/', views.department_list.as_view()),
    path('department/<int:pk>/', views.department_individual.as_view()),
    path('employees/', views.employee_list.as_view()),
    path('employee/<int:pk>/', views.employee_individual.as_view()),
]