from django import forms

class form_user(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control ','placeholder': "Name"}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Last-name'}))
    mail = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control mb-4 px-1','placeholder':'E-mail'}))
    phone =forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control px-1','placeholder': 'Phone-number'}))