from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)
    tel = forms.CharField(max_length=18)

    class Meta:
        model = User
        fields = ['username', 'name', 'surname', 'email', 'tel', 'password1', 'password2']


class Contact_us(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField(required=True)
    text = forms.CharField(widget=forms.Textarea, max_length=800)
