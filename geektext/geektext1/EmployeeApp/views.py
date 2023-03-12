from rest_framework import generics
from .models import Book, Comments, Rating
from .serializers import BookSerializer, CommentSerializer, RatingSerializer


class book_list(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class book_individual(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class comment_list(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

class comment_individual(generics.RetrieveUpdateDestroyAPIView):    
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

class rating_list(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class rating_individual(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
