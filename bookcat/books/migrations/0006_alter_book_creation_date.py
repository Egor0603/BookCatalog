# Generated by Django 4.0.4 on 2022-05-15 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_author_remove_book_author_authorbook_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='creation_date',
            field=models.IntegerField(),
        ),
    ]