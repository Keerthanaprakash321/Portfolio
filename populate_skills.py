
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
django.setup()

from accounts_app.models import Skill

def populate_skills():
    print("Clearing existing skills...")
    Skill.objects.all().delete()

    skills_data = [
        # Languages
        {'name': 'Python', 'category': 'LANGUAGE', 'is_key_skill': True},
        {'name': 'C++', 'category': 'LANGUAGE', 'is_key_skill': True},
        {'name': 'C', 'category': 'LANGUAGE', 'is_key_skill': False},

        # Tools/Platforms
        {'name': 'VS Code', 'category': 'TOOL', 'is_key_skill': True},
        {'name': 'Wireshark', 'category': 'TOOL', 'is_key_skill': True},
        {'name': 'Debian', 'category': 'TOOL', 'is_key_skill': False},

        # Soft Skills
        {'name': 'Problem-Solving', 'category': 'SOFT_SKILL', 'is_key_skill': True},
        {'name': 'Critical thinking', 'category': 'SOFT_SKILL', 'is_key_skill': True},
        {'name': 'Adaptability', 'category': 'SOFT_SKILL', 'is_key_skill': True},
    ]

    print("Adding new skills...")
    for skill_info in skills_data:
        Skill.objects.create(**skill_info)
        print(f"Added: {skill_info['name']} ({skill_info['category']})")

    print("Done!")

if __name__ == '__main__':
    populate_skills()
