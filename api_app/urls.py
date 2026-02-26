from django.urls import path
from .views import (
    ProjectListCreateView, ProjectDetailView, 
    ContactCreateView, 
    SkillListCreateView, SkillDetailView,
    CertificateListCreateView, CertificateDetailView,
    EducationListCreateView, EducationDetailView,
    ExperienceListCreateView, ExperienceDetailView,
    BlogListCreateView, BlogDetailView
)

urlpatterns = [
    path('projects/', ProjectListCreateView.as_view(), name='api_project_list'),
    path('projects/<slug:slug>/', ProjectDetailView.as_view(), name='api_project_detail'),
    path('skills/', SkillListCreateView.as_view(), name='api_skill_list'),
    path('skills/<int:pk>/', SkillDetailView.as_view(), name='api_skill_detail'),
    path('certificates/', CertificateListCreateView.as_view(), name='api_certificate_list'),
    path('certificates/<int:pk>/', CertificateDetailView.as_view(), name='api_certificate_detail'),
    path('education/', EducationListCreateView.as_view(), name='api_education_list'),
    path('education/<int:pk>/', EducationDetailView.as_view(), name='api_education_detail'),
    path('experience/', ExperienceListCreateView.as_view(), name='api_experience_list'),
    path('experience/<int:pk>/', ExperienceDetailView.as_view(), name='api_experience_detail'),
    path('blogs/', BlogListCreateView.as_view(), name='api_blog_list'),
    path('blogs/<slug:slug>/', BlogDetailView.as_view(), name='api_blog_detail'),
    path('contact/', ContactCreateView.as_view(), name='api_contact_create'),
]
