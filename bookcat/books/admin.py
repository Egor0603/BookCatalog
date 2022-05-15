from django.contrib import admin
from .models import Book

admin.site.register(Book) # регистрируем модель для взаимодействия с ней в админ панели
