import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
django.setup()

from django.contrib.auth.models import User
from accounts_app.models import Profile

def fix_profiles():
    users = User.objects.all()
    count = 0
    for user in users:
        try:
            user.profile
        except Profile.DoesNotExist:
            print(f"Creating profile for user: {user.username}")
            Profile.objects.create(user=user)
            count += 1
    
    print(f"Fixed {count} users without profiles.")

if __name__ == "__main__":
    fix_profiles()
