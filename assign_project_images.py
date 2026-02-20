import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
django.setup()

from projects_app.models import Project

# Map: display order (newest first, same as page) → image path relative to MEDIA_ROOT
image_map = {
    0: 'projects/book_recommendation.png',
    1: 'projects/parking_allocator.png',
    2: 'projects/coffee_bakery.jpg',
}

projects = list(Project.objects.all().order_by('-created_date'))
print(f"Found {len(projects)} projects:")
for i, p in enumerate(projects):
    print(f"  [{i}] ID={p.id}  Title={p.title}  Current image={p.image}")

for idx, img_path in image_map.items():
    if idx < len(projects):
        proj = projects[idx]
        proj.image = img_path
        proj.save()
        print(f"  ✅ Set '{img_path}' on project [{idx}]: {proj.title}")
    else:
        print(f"  ⚠️  No project at index {idx}")

print("Done!")
