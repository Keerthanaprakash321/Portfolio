from django.urls import path
from .views import ProjectListCreateView, ProjectDetailView, ContactCreateView

urlpatterns = [
    path('projects/', ProjectListCreateView.as_view(), name='api_project_list'),
    path('projects/<slug:slug>/', ProjectDetailView.as_view(), name='api_project_detail'),
    path('contact/', ContactCreateView.as_view(), name='api_contact_create'),
]
