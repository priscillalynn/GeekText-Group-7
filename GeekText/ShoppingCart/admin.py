from django.contrib import admin
from ShoppingCart import models

# Register your models here.

# Registers the models from the database to allow them to be viewed in the admin panel
admin.site.register(models.Users)
admin.site.register(models.Books)
