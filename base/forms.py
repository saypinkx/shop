from django import forms


class SignUpForm(forms.Form):
    name = forms.CharField(min_length=1, max_length=30, required=True,
                           widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    surname = forms.CharField(min_length=1, max_length=30, required=True,
                              widget=forms.TextInput(attrs={'placeholder': 'Surname'}))
    email = forms.EmailField(min_length=1, max_length=30, required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(min_length=1, max_length=30, required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
