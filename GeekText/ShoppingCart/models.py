from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Users(models.Model):
    UserId = models.AutoField(primary_key = True)
    # not sure if i should include username and password because django has functionality to handle elsewhere
    Username = models.CharField(max_length=500)
    Password = models.CharField(max_length=500)
    Name = models.CharField(max_length=500, null=True, blank=True)
    Email = models.EmailField(max_length=500, null=True, blank=True)
    HomeAddress = models.TextField(max_length=500, null=True, blank=True)

class Books(models.Model):
    BookISBN = models.CharField(max_length=13)
    BookName = models.CharField(max_length=500)
    BookDescription = models.CharField(max_length=2000)
    # maybe create min and max price later
    BookPrice = models.IntegerField(default=0)
    Author = models.CharField(max_length=500)
    BookGenre = models.CharField(max_length=500)
    BookPublisher = models.CharField(max_length=500)
    YearPublished = models.DateField()
    CopiesSold = models.IntegerField(default=0)
    # maybe set max book rating to 5 later
    BookRating = models.IntegerField(default=0)
