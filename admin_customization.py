from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'tech_stack')
    search_fields = ('title', 'description', 'tech_stack')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created_date',)

# Contact App Admin
from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'timestamp', 'is_read')
    search_fields = ('name', 'email', 'subject', 'message')
    list_filter = ('is_read', 'timestamp')
