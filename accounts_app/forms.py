from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Certificate



class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['title', 'issuer', 'date_issued', 'description', 'credential_url', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full px-3 py-2 bg-black border border-[var(--border-color)] rounded focus:outline-none focus:border-[var(--text-primary)] text-white'}),
            'issuer': forms.TextInput(attrs={'class': 'w-full px-3 py-2 bg-black border border-[var(--border-color)] rounded focus:outline-none focus:border-[var(--text-primary)] text-white'}),
            'date_issued': forms.DateInput(attrs={'class': 'w-full px-3 py-2 bg-black border border-[var(--border-color)] rounded focus:outline-none focus:border-[var(--text-primary)] text-white', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'w-full px-3 py-2 bg-black border border-[var(--border-color)] rounded focus:outline-none focus:border-[var(--text-primary)] text-white', 'rows': 3}),
            'credential_url': forms.URLInput(attrs={'class': 'w-full px-3 py-2 bg-black border border-[var(--border-color)] rounded focus:outline-none focus:border-[var(--text-primary)] text-white'}),
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full px-3 py-2 bg-black border border-[var(--border-color)] rounded focus:outline-none focus:border-[var(--text-primary)] text-white'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'w-full px-3 py-2 bg-black border border-[var(--border-color)] rounded focus:outline-none focus:border-[var(--text-primary)] text-white'}))
