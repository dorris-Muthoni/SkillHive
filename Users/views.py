from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm, RegisterForm
from .models import Skill, UserProfile

def home(request):
    """Render the homepage."""
    return render(request, 'home.html')

def register(request):
    """User registration view using RegisterForm."""
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('login')
        else:
            # Display errors from the form
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


def login_user(request):
    """User login view using LoginForm."""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Extract username and password from the form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Attempt to authenticate the user
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Authentication successful, log the user in
                login(request, user)
                messages.success(request, "You have successfully logged in.")
                return redirect('profile')  # Redirect to the profile page after login
            else:
                # Authentication failed, show an error message
                messages.error(request, "Invalid username or password.")
                return redirect('login')  # Redirect back to the login page if login fails
    else:
        form = LoginForm()  # If GET request, show an empty form

    return render(request, 'Users/templates/login.html', {'form': form})
def about(request):
    """Render the About Us page."""
    return render(request, 'about.html', {'title': 'About Us'})

def logout_user(request):
    """User logout view."""
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('home')

@login_required
def profile(request):
    """Render the user's profile."""
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = None  # Handle missing profiles gracefully
    return render(request, 'profile.html', {'profile': user_profile})

@login_required
def skills(request):
    """View or update shared skills."""
    if request.method == 'POST':
        skill_name = request.POST.get('skill_name')
        if skill_name:
            # Add a new skill (assuming the `Skill` model has fields `name` and `user`)
            Skill.objects.create(user=request.user, name=skill_name)
            messages.success(request, "Skill added successfully!")

    # Get the user's skills
    user_skills = Skill.objects.filter(user=request.user)
    return render(request, 'skills.html', {'skills': user_skills})


@login_required
def update_profile(request):
    # Logic for updating the user profile will go here
    return render(request, 'update_profile.html') 

@login_required
def book_session(request):
    # Logic for booking a session goes here
    return render(request, 'book_session.html') 
