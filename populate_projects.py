import os
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
django.setup()

from projects_app.models import Project

def populate_projects():
    projects = [
        {
            "title": "Network Vulnerability Scanner",
            "description": "Developed a Python-based network scanner to identify open ports and potential vulnerabilities in local networks. The tool uses `scapy` and `socket` libraries to map network topology and flag insecure services.",
            "tech_stack": "Python Scapy TCP/IP Networking",
            "github_link": "https://github.com/keerthana/network-scanner",
            "live_link": "",
        },
        {
            "title": "Secure Chat Application",
            "description": "Designed and implemented an end-to-end encrypted chat application using AES-256 encryption. Features include secure key exchange, message integrity verification, and ephemeral messaging.",
            "tech_stack": "Python Cryptography PyCrypto Socket Programming",
            "github_link": "https://github.com/keerthana/secure-chat",
            "live_link": "",
        },
        {
            "title": "Phishing Detection System",
            "description": "Built a machine learning model to classify emails as phishing or legitimate based on header analysis and content features. Achieved 95% accuracy using Random Forest classifier.",
            "tech_stack": "Python Scikit-Learn Pandas Machine Learning",
            "github_link": "https://github.com/keerthana/phishing-detector",
            "live_link": "",
        },
        {
            "title": "Django Web Security Audit",
            "description": "Conducted a comprehensive security audit of a Django e-commerce platform. Identified and patched SQL Injection points, XSS vulnerabilities, and misconfigured CSRF settings.",
            "tech_stack": "Django OWASP_ZAP Burp_Suite Web_Security",
            "github_link": "https://github.com/keerthana/security-audit",
            "live_link": "",
        }
    ]

    for p_data in projects:
        project, created = Project.objects.get_or_create(
            title=p_data["title"],
            defaults={
                "description": p_data["description"],
                "tech_stack": p_data["tech_stack"],
                "github_link": p_data["github_link"],
                "live_link": p_data["live_link"],
                "created_date": date.today()
            }
        )
        if created:
            print(f"Created project: {project.title}")
        else:
            print(f"Project already exists: {project.title}")

if __name__ == "__main__":
    populate_projects()
