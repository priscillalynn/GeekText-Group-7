from django.contrib import admin
from django.urls import path
from EmployeeApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', views.book_list.as_view()),
    path('book/<int:pk>/', views.book_individual.as_view()),
    path('comments/', views.comment_list.as_view()),
    path('comment/<int:pk>/', views.comment_individual.as_view()),
    path('ratings/', views.rating_list.as_view()),
    path('rating/<int:pk>/', views.rating_individual.as_view()),
]