from django.forms import ModelForm, ModelMultipleChoiceField, BooleanField

from .models import Book


class BookForm(ModelForm): # форма для создания новый записей в нашей бд с самого сайта
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Choose category' # вместо "------" в поле выбора категории будет "Choose category"
        self.fields['author'].empty_label = 'Choose author'

    check_box = BooleanField(label='Checked!') # добавит кнопку, которую нужно нажать перед созданием записи

    class Meta:
        model = Book
        fields = ['name', 'author', 'category', 'creation_date', 'text', 'check_box'] # поля, которые нужно будет заполнить при создании

