from rest_framework import serializers
from .models import Book, Comments, Rating

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'author', 'description', 'published_date', 'isbn_number')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('user', 'book', 'comment', 'created_at')

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('user', 'book', 'rating', 'created_at')