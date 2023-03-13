from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

'''
Model for Book information in database. Uses model.model to create blank model. Adds fields for BookISBN, name,
description, price, author, genre, publisher, year of publishing, copies sold, and rating. Sets a default value of 0 
for integer fields price, copies sold, and rating. 
'''
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


'''
Model for User information in database. Uses AbstractUser module to handle the common user info like name, password,
email. Adds field for name and home address. 
'''
class Users(AbstractUser):
    Name = models.CharField(max_length=500, null=True, blank=True)
    HomeAddress = models.TextField(max_length=500, null=True, blank=True)
    Cart = models.ManyToManyField(Books, blank=True, default=list)

    def GetCart(self):
        return self.Cart.all()

    def TotalPrice(self):
        total = 0

        if self.Cart.__sizeof__() == 0:
            return total
        else:
            for book in self.Cart.all():
                total += book.BookPrice

            return total


