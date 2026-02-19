from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

# Only staff should create/manage projects for a portfolio
def is_staff(user):
    return user.is_staff

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects_app/project_list.html', {'projects': projects})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'projects_app/project_detail.html', {'project': project})

@login_required
@user_passes_test(is_staff)
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save()
            messages.success(request, 'Project created successfully!')
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'projects_app/project_form.html', {'form': form, 'title': 'Add Project'})

@login_required
@user_passes_test(is_staff)
def update_project(request, slug):
    project = get_object_or_404(Project, slug=slug)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated successfully!')
            return redirect('project_detail', slug=project.slug)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'projects_app/project_form.html', {'form': form, 'title': 'Edit Project', 'project': project})

@login_required
@user_passes_test(is_staff)
def delete_project(request, slug):
    project = get_object_or_404(Project, slug=slug)
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project deleted successfully!')
        return redirect('project_list')
    return render(request, 'projects_app/project_confirm_delete.html', {'project': project})
