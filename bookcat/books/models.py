from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return str(self.name)


class Category(models.Model):
    name = models.CharField(default='Unknown category', max_length=50, unique=True)

    def __str__(self):
        return str(self.name)


class Book(models.Model):
    author = models.ManyToManyField(Author, through='AuthorBook')
    name = models.CharField(max_length=50)
    creation_date = models.IntegerField()
    category = models.ManyToManyField(Category, through='CategoryBook')
    text = models.TextField(null=True)

    def __str__(self):
        return str(self.name)

    @classmethod
    def get_absolute_url(cls): # возвращает нас на основную страницу после добавления книги
        return '/books/'


class CategoryBook(models.Model): # с помощью этой модели реализуем связь многие ко многим
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


class AuthorBook(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


