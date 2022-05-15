from django.contrib import admin
from .models import Book, Author

admin.site.register(Book) # регистрируем модель для взаимодействия с ней в админ панели
admin.site.register(Author)
