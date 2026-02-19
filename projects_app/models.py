from django.db import models
from django.utils.text import slugify

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=255, help_text="e.g. Django, React, PostgreSQL")
    github_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)
    created_date = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    
    class Meta:
        ordering = ['-created_date']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
