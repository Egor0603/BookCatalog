from django.forms import SelectDateWidget
from django_filters import FilterSet, DateFilter, ModelMultipleChoiceFilter, CharFilter
from .models import Book, Category


class BookFilter(FilterSet): #фильтр для поиска по списку
    category = ModelMultipleChoiceFilter(queryset=Category.objects.all())
    name = CharFilter(label='Name', lookup_expr='icontains') # icontains означает, что ищем похожее на то, что ввели в поле поиска
    author = CharFilter(label='Author', lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['name', 'author', 'category']
