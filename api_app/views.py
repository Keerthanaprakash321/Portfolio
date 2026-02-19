from rest_framework import generics, permissions
from projects_app.models import Project
from contact_app.models import ContactMessage
from .serializers import ProjectSerializer, ContactMessageSerializer

class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # Allow read to all, create to auth (using IsAuthenticatedOrReadOnly which is standard)

class ProjectDetailView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny] # Allow detail view to all
    lookup_field = 'slug'

class ContactCreateView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [permissions.AllowAny] # Allow anyone to submit contact form via API
