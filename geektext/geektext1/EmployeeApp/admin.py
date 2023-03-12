from django.contrib import admin
from .models import Book, Comments, Rating

admin.site.register(Book)
admin.site.register(Comments)
admin.site.register(Rating)

class BookAdmin(admin.ModelAdmin):
    fields = ('title', 'author', 'description', 'published_date', 'isbn_number')

class CommentAdmin(admin.ModelAdmin):
    fields = ('user', 'book', 'comment', 'created_at')

class RatingAdmin(admin.ModelAdmin):
    fields = ('user', 'book', 'rating', 'created_at')