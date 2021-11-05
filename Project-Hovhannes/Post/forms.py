from django import forms

class Contact_us(forms.Form):

    name = forms.CharField(max_length=20)
    email = forms.EmailField(required=True)
    text = forms.CharField(widget=forms.Textarea, max_length=800)