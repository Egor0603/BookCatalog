from django.shortcuts import render
from django.views.generic import ListView, CreateView

from .filters import BookFilter
from .forms import BookForm
from .models import Book


class BookList(ListView): # представление, что будет выводить объекты бд на страницу
    model = Book
    template_name = 'search.html'
    context_object_name = 'books' # переменная в шаблоне, через которую будем обращаться к модели
    queryset = Book.objects.order_by('-id') # отображение будет в порядке убывания id
    paginate_by = 3

    # подключаем наш фильтр к нужному представлению для поиска
    def get_filter(self):
        return BookFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *args, **kwargs):
        return {
            **super().get_context_data(*args, **kwargs),
            'filter': self.get_filter()
        }


# дополнительное представление, создающее новые записи с помощью формы
class BookCreate(CreateView):
    form_class = BookForm
    template_name = 'book_create.html'
