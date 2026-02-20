
import os
import shutil
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
django.setup()

from projects_app.models import Project

def add_image():
    # Source image (Artifact)
    source_path = r'C:\Users\keert\.gemini\antigravity\brain\f8691388-34d9-4398-82c4-52d257db4d9b\media__1771526215429.png'
    
    # Destination directory
    media_dir = r'c:\Users\keert\Portfolio\media\projects'
    os.makedirs(media_dir, exist_ok=True)
    
    # Destination file
    dest_filename = 'parking_allocator.png'
    dest_path = os.path.join(media_dir, dest_filename)
    
    # Copy file
    if os.path.exists(source_path):
        shutil.copy2(source_path, dest_path)
        print(f"Copied image to {dest_path}")
    else:
        print(f"Error: Source file not found at {source_path}")
        return

    # Update Project
    try:
        project = Project.objects.get(title__iexact="Real time Parking slot Allocator")
        project.image = f'projects/{dest_filename}'
        project.save()
        print(f"Successfully updated project '{project.title}' with image.")
    except Project.DoesNotExist:
        print("Error: Project 'Real time Parking slot Allocator' not found.")
    except Exception as e:
        print(f"Error updating project: {e}")

if __name__ == "__main__":
    add_image()
