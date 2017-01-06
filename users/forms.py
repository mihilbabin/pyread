from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Profile

class UserForm(forms.ModelForm):
    confirm_password = forms.CharField()
    password = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password')

    def clean(self):
        if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
            raise ValidationError("Passwords didn't match.")
        return self.cleaned_data

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('website', 'image')
        widgets = {
            'website': forms.TextInput(attrs={'class': 'form-control'})
        }

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
