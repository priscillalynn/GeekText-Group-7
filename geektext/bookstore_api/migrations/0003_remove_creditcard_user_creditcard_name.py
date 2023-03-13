# Generated by Django 4.1.7 on 2023-02-22 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore_api', '0002_load_dummy_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creditcard',
            name='user',
        ),
        migrations.AddField(
            model_name='creditcard',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
