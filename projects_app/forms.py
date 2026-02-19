from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'tech_stack', 'github_link', 'live_link', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:border-blue-500'}),
            'description': forms.Textarea(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:border-blue-500', 'rows': 5}),
            'tech_stack': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:border-blue-500', 'placeholder': 'e.g. Django, React, PostgreSQL'}),
            'github_link': forms.URLInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:border-blue-500'}),
            'live_link': forms.URLInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:border-blue-500'}),
            'image': forms.FileInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:border-blue-500'}),
        }
