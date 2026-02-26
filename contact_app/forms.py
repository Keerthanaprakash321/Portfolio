from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-3 py-2 bg-black border border-[var(--border-color)] rounded focus:outline-none focus:border-[var(--text-primary)] text-white'}),
            'email': forms.EmailInput(attrs={'class': 'w-full px-3 py-2 bg-black border border-[var(--border-color)] rounded focus:outline-none focus:border-[var(--text-primary)] text-white'}),
            'subject': forms.TextInput(attrs={'class': 'w-full px-3 py-2 bg-black border border-[var(--border-color)] rounded focus:outline-none focus:border-[var(--text-primary)] text-white'}),
            'message': forms.Textarea(attrs={'class': 'w-full px-3 py-2 bg-black border border-[var(--border-color)] rounded focus:outline-none focus:border-[var(--text-primary)] text-white', 'rows': 5}),
        }
