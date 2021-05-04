from django import forms


class UserForm(forms.Form):
    name = forms.CharField(max_length=64)
    surname = forms.CharField(max_length=128)
    email = forms.EmailInput()
    username = forms.CharField(max_length=128)
    password = forms.PasswordInput()

