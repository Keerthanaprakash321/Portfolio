from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Profile, Skill, Education, Experience, Certificate
from .forms import SignUpForm, LoginForm, CertificateForm

from projects_app.models import Project

import os
from pathlib import Path

def home(request):
    try:
        print(f"DEBUG_CWD: {os.getcwd()}")
        print(f"DEBUG_BASE_DIR: {settings.BASE_DIR}")
        print(f"DEBUG_TEMPLATE_DIR: {settings.BASE_DIR / 'templates'}")
        profile = Profile.objects.first()
        skills = Skill.objects.all()
        projects = Project.objects.all()
        print(f"DEBUG_COUNT: profile={profile}, skills={skills.count()}, projects={projects.count()}")
        for s in skills:
            print(f"DEBUG_SKILL: {s.name} ({s.category})")
        for p in projects:
            print(f"DEBUG_PROJECT: {p.title} - desc_len={len(p.description)}")
    except Exception as e:
        print(f"DEBUG_ERROR: {e}")
        profile = None
        skills = []
        projects = []
    
    context = {
        'profile': profile,
        'skills': skills,
        'projects': projects,
    }
    return render(request, 'accounts_app/home.html', context)

def about(request):
    try:
        profile = Profile.objects.first()
        education = Education.objects.filter(profile=profile)
        experience = Experience.objects.filter(profile=profile)
        skills = Skill.objects.all()
    except Exception:
        profile = None
        education = []
        experience = []
        skills = []

    context = {
        'profile': profile,
        'education': education,
        'experience': experience,
        'skills': skills,
    }
    return render(request, 'accounts_app/about.html', context)

@login_required
@user_passes_test(lambda u: u.is_staff)
def dashboard(request):
    try:
        profile = request.user.profile
        certificates = Certificate.objects.filter(profile=profile)
    except Exception:
        certificates = []
    
    return render(request, 'accounts_app/dashboard.html', {'certificates': certificates})

@login_required
@user_passes_test(lambda u: u.is_staff)
def create_certificate(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST, request.FILES)
        if form.is_valid():
            certificate = form.save(commit=False)
            certificate.profile = request.user.profile
            certificate.save()
            messages.success(request, 'Certificate added successfully!')
            return redirect('dashboard')
    else:
        form = CertificateForm()
    return render(request, 'accounts_app/certificate_form.html', {'form': form, 'title': 'Add Certificate'})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'accounts_app/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            if user.email:
                try:
                    send_mail(
                        subject="Welcome Back!",
                        message=f"Hi {user.username},\n\nThank you for logging in to your portfolio account. We're glad to have you back!\n\nBest regards,\nKeerthana",
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        recipient_list=[user.email],
                        fail_silently=True,
                    )
                except Exception as e:
                    print(f"Login email failed: {e}")

            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'accounts_app/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        user_email = request.user.email
        user_name = request.user.username
        
        logout(request)
        
        if user_email:
            try:
                send_mail(
                    subject="Thank You for Visiting",
                    message=f"Hi {user_name},\n\nThank you for visiting my portfolio. I hope to see you again soon!\n\nBest regards,\nKeerthana",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[user_email],
                    fail_silently=True,
                )
            except Exception as e:
                print(f"Logout email failed: {e}")

        messages.info(request, "Logged out successfully!")
        return redirect('home')
    return redirect('home')
