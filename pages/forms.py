from django import forms
from .models import Category, Page


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'name': 'Please enter Category name',
        }


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ('title', 'url')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.TextInput(attrs={'class': 'form-control'})
        }
        help_texts = {
            'title': 'Please enter title of the page',
            'url': 'Please enter the URL of the page'
        }

    def clean_url(self):
        url = self.cleaned_data.get('url')
        if url and not url.startswith('http://'):
            url = 'http://' + url
        return url
