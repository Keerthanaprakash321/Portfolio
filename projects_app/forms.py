from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'tech_stack', 'github_link', 'live_link', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full px-3 py-2 bg-black border border-[var(--border-color)] rounded focus:outline-none focus:border-[var(--text-primary)] text-white'}),
            'description': forms.Textarea(attrs={'class': 'w-full px-3 py-2 bg-black border border-[var(--border-color)] rounded focus:outline-none focus:border-[var(--text-primary)] text-white', 'rows': 5}),
            'tech_stack': forms.TextInput(attrs={'class': 'w-full px-3 py-2 bg-black border border-[var(--border-color)] rounded focus:outline-none focus:border-[var(--text-primary)] text-white', 'placeholder': 'e.g. Django, React, PostgreSQL'}),
            'github_link': forms.URLInput(attrs={'class': 'w-full px-3 py-2 bg-black border border-[var(--border-color)] rounded focus:outline-none focus:border-[var(--text-primary)] text-white'}),
            'live_link': forms.URLInput(attrs={'class': 'w-full px-3 py-2 bg-black border border-[var(--border-color)] rounded focus:outline-none focus:border-[var(--text-primary)] text-white'}),
            'image': forms.FileInput(attrs={'class': 'w-full px-3 py-2 bg-black border border-[var(--border-color)] rounded focus:outline-none focus:border-[var(--text-primary)] text-white'}),
        }
