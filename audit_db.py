
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
django.setup()

from django.apps import apps
from django.db.models import CharField, TextField

def audit_models():
    found_tags = False
    for app_config in apps.get_app_configs():
        if app_config.name in ['accounts_app', 'projects_app', 'blog_app', 'contact_app']:
            print(f"Auditing app: {app_config.name}")
            for model in app_config.get_models():
                print(f"  Checking model: {model.__name__}")
                fields = [f.name for f in model._meta.get_fields() if isinstance(f, (CharField, TextField))]
                for obj in model.objects.all():
                    for field in fields:
                        val = getattr(obj, field)
                        if val and ('{{' in val or '{%' in val):
                            print(f"    !!! FOUND TAG in {model.__name__} (ID: {obj.pk}, Field: {field}):")
                            print(f"        Value: {val}")
                            found_tags = True
    
    if not found_tags:
        print("No literal template tags found in any inspected model fields.")

if __name__ == "__main__":
    audit_models()
