import os
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
django.setup()

from projects_app.models import Project

def populate_projects():
    # Clear existing projects to showcase only user's real projects
    print("Clearing existing projects...")
    Project.objects.all().delete()

    projects = [
        {
            "title": "Coffee and Bakery Website",
            "description": "Designed and developed a responsive Coffee and bakery Website to showcase items, pricing, and appointment options. Gained strong technical experience in frontend development such as HTML, CSS, JavaScript and Dynamic UI designs. Implemented interactive features, mobile-friendly design, UI/UX with modern layouts, improving user browsing experience.",
            "tech_stack": "HTML CSS JavaScript Dynamic_UI",
            # User provided credentials but missed the specific link for this project.
            # Using a placeholder or the main profile for now.
            "github_link": "https://github.com/Keerthanaprakash321/Cofee-and-bakery-Website/tree/main", 
            "live_link": "",
        },
        {
            "title": "Real time Parking slot Allocator",
            "description": "Built a Real time parking slot allocator using CPP to manage vehicles of all types in an efficient and sustainable way. Implemented secure role-based login for vehicle owner to ensure controlled access. Gained knowledge about backend modules and database queries, improving data retrieval speed and overall system efficiency. Implemented interactive features and efficient parking slot for all kinds of vehicles.",
            "tech_stack": "C++ Database Backend Security",
            "github_link": "https://github.com/Keerthanaprakash321/Real-time-parking-slot-allocator/tree/main",
            "live_link": "",
        },
        {
            "title": "Book Recommendation Website",
            "description": "Designed and developed an interactive Book Recommendation Website that allows users to explore, search, and receive personalized book suggestions based on genres, ratings, and user preferences. Gained strong technical experience in frontend development such as HTML, CSS, JavaScript and Dynamic UI designs. Delivered a responsive and user-friendly platform that improves user engagement, provides accurate book recommendations, and enhances browsing experience across multiple devices.",
            "tech_stack": "HTML CSS JavaScript Dynamic_UI",
            "github_link": "https://github.com/Keerthanaprakash321/Book-Recommendation-Website",
            "live_link": "",
        },
    ]

    print("Adding new projects...")
    for p_data in projects:
        project = Project.objects.create(
            title=p_data["title"],
            description=p_data["description"],
            tech_stack=p_data["tech_stack"],
            github_link=p_data["github_link"],
            live_link=p_data["live_link"],
            created_date=date.today()
        )
        print(f"Created project: {project.title}")

    print("Done!")

if __name__ == "__main__":
    populate_projects()
