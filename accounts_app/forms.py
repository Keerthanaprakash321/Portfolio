from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        # Add widget attrs for styling
        widgets = {
            'username': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:border-blue-500'}),
            'first_name': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:border-blue-500'}),
            'last_name': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:border-blue-500'}),
            'email': forms.EmailInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:border-blue-500'}),
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:border-blue-500'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:border-blue-500'}))
