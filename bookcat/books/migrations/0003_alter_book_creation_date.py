# Generated by Django 4.0.4 on 2022-05-14 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='creation_date',
            field=models.DateTimeField(),
        ),
    ]
