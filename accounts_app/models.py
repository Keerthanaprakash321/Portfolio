from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, help_text="Short bio about yourself.")
    short_intro = models.TextField(blank=True, help_text="Short introduction for the home page.")
    resume = models.FileField(upload_to='resumes/', blank=True, null=True, help_text="Upload your resume (PDF).")
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True, help_text="Profile picture.")
    skills = models.CharField(max_length=255, blank=True, help_text="Comma-separated list of skills (deprecated, use Skill model).")
    linkedin_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"

class Skill(models.Model):
    name = models.CharField(max_length=100)
    is_key_skill = models.BooleanField(default=False, help_text="Check if this is a key skill to show on the home page.")

    def __str__(self):
        return self.name

class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True, help_text="Leave blank if currently pursuing.")
    description = models.TextField(blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='education')

    class Meta:
        ordering = ['-end_date', '-start_date']

    def __str__(self):
        return f"{self.degree} at {self.institution}"

class Experience(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True, help_text="Leave blank if currently working there.")
    description = models.TextField(blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='experience')

    class Meta:
        ordering = ['-end_date', '-start_date']

    def __str__(self):
        return f"{self.role} at {self.company}"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
