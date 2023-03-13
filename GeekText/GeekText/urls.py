"""GeekText URL Configuration

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
from ShoppingCart import views

'''
Creates URL paths for each view. users/ will return a list of all users and allow for new user creation using the 
UserList view. users/<int:pk>/ will return a single user, update single user information, 
or destroy a user using its ID in the database through the UserIndividual view. books/ will return a list of all books 
or allow for new user creation using the BookList view. books/<int:pk>/ will return a single book, update single book 
information, or destroy a book using its ID in the database through the BookIndividual view
'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserIndividual.as_view()),
    path('users/<int:user_id>/cart/', views.UserShoppingCartList.as_view()),
    path('users/<int:user_id>/atc/<int:book_id>/', views.UserAddBookToCart.as_view()),
    path('users/<int:user_id>/remove/<int:book_id>/', views.UserRemoveBookFromCart.as_view()),
    path('users/<int:user_id>/cart/total/', views.UserShoppingCartTotal.as_view()),
    path('books/', views.BookList.as_view()),
    path('books/<int:pk>/', views.BookIndividual.as_view()),
]
