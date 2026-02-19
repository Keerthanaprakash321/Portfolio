from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'tech_stack', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'description', 'tech_stack')
    list_filter = ('created_date',)
