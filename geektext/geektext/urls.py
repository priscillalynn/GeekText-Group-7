"""geektext URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bookstore_api import views
from bookstore_api.views import CreateUserView
from bookstore_api.views import GetUserView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserIndividual.as_view()),
    path('creditcard/', views.CreditCardList.as_view()),
    path('creditcard/<int:pk>/', views.CreditCardIndividual.as_view()),
    path('users/', CreateUserView.as_view(), name='create_user'),
    path('users/<str:username>/', GetUserView.as_view()),
]
