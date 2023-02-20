from rest_framework import serializers
from ShoppingCart.models import Users, Books

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('UserId', 'Username', 'Password', 'Name', 'Email', 'HomeAddress')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('BookISBN', 'BookName', 'BookDescription', 'BookPrice', 'Author', 'BookGenre', 'BookPublisher', 'YearPublished', 'CopiesSold', 'BookRating')