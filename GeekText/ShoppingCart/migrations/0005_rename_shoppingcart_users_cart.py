# Generated by Django 4.1.7 on 2023-03-12 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShoppingCart', '0004_alter_users_shoppingcart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='ShoppingCart',
            new_name='Cart',
        ),
    ]
