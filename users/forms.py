from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import User

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields =['full_name','email','avatar','password','confirm_password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords don't match")

        return cleaned_data


class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email')

    class Meta:
        fields = ['username','password']