from django import forms


class SignUpForm(forms.Form):
    name = forms.CharField(min_length=1, max_length=30, required=False,
                           widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    surname = forms.CharField(min_length=1, max_length=30, required=False,
                              widget=forms.TextInput(attrs={'placeholder': 'Surname'}))
    email = forms.EmailField(min_length=1, max_length=30, required=False,
                             widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(min_length=1, max_length=30, required=False,
                               widget=forms.TextInput(attrs={'placeholder': 'password'}))
