from rest_framework import serializers
from ShoppingCart.models import Users, Books

'''
Serializer for Users model. This is what determines the response to GET requests. Sets the model as Users from models.py,
sets the output fields as the ID, username, first name, last name, and home address. 
'''
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'username','first_name', 'last_name', 'HomeAddress')

'''
Serializer for Books model. This is what determines the response to GET requests. Sets the model as Books from models.py,
sets the output fields as the BookISBN, BookName, BookDescription, BookPrice, Author, BookGenre, BookPublisher, 
YearPublished, CopiesSold, and BookRating. 
'''
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('BookISBN', 'BookName', 'BookDescription', 'BookPrice', 'Author', 'BookGenre', 'BookPublisher', 'YearPublished', 'CopiesSold', 'BookRating')

'''
Serializer for Total Price. This is what determines the response to GET requests. Sets the total_price as a FloatField()
and the cart_items as a BookSerializer object and enables processing of multiple objects 
'''
class UserTotalPriceSerializer(serializers.Serializer):
    total_price = serializers.FloatField()
    cart_items = BookSerializer(many=True)