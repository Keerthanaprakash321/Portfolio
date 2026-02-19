from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:border-blue-500'}),
            'email': forms.EmailInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:border-blue-500'}),
            'subject': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:border-blue-500'}),
            'message': forms.Textarea(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:border-blue-500', 'rows': 5}),
        }
