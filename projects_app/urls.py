from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_project, name='create_project'),
    path('<slug:slug>/', views.project_detail, name='project_detail'),
    path('<slug:slug>/update/', views.update_project, name='update_project'),
    path('<slug:slug>/delete/', views.delete_project, name='delete_project'),
]
