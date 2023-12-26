from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
#from django import forms
class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']
        widgets = {
            "title":TextInput(attrs={
                'class':'form-control',
                'placeholder':'Назва'
            }),
            "anons":TextInput(attrs={
                'class':'form-control',
                'placeholder':'Анонс'
            }),
            "date":DateTimeInput(attrs={
                'class':'form-control',
                'placeholder':'Дата публікації'
            }),
            "full_text":Textarea(attrs={
                'class': 'form-control',
                'placeholder':'Текст статті'
            })
        }