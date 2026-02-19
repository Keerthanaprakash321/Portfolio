from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile, Skill, Education, Experience
from .forms import SignUpForm, LoginForm

def home(request):
    try:
        profile = Profile.objects.first() # Simplest for now, getting the first profile
        skills = Skill.objects.filter(is_key_skill=True)
    except Exception:
        profile = None
        skills = []
    
    context = {
        'profile': profile,
        'skills': skills,
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
def dashboard(request):
    return render(request, 'accounts_app/dashboard.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'accounts_app/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST) # AuthenticationForm takes request as first arg but data= is clearer here or (request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'accounts_app/login.html', {'form': form})

from django.conf import settings
from django.core.mail import send_mail

def logout_view(request):
    if request.method == 'POST':
        # Capture user info before logout
        user_email = request.user.email
        user_name = request.user.username
        
        logout(request)
        
        # Send Thank You Email
        if user_email:
            try:
                send_mail(
                    subject="Thank You for Visiting",
                    message=f"Hi {user_name},\n\nThank you for visiting my portfolio. I hope to see you again soon!\n\nBest regards,\nKeerthana",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[user_email],
                    fail_silently=True, # Don't crash logout if email fails
                )
            except Exception as e:
                print(f"Logout email failed: {e}")

        messages.info(request, "Logged out successfully!")
        return redirect('home')
    return redirect('home')
