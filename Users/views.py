from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm, RegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib import messages 
from .models import Skill, UserProfile , Booking 
from django.shortcuts import redirect, get_object_or_404
from .forms import SkillForm


def home(request):
    """Render the homepage."""
    return render(request, 'home.html')

def manage_skills(request):
    return render(request, 'skills.html')

def book_session(request):
    return render(request, 'book_session.html')

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
        messages.info(request, "You don't have a profile yet, please create one.")

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
 
@login_required
def manage_skills(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'add':
            name = request.POST.get('name')
            description = request.POST.get('description')
            
            # Get the logged-in user's profile
            user_profile = UserProfile.objects.get(user=request.user)

            # Create the new skill and associate it with the user profile
            skill = Skill.objects.create(
                name=name,
                description=description
            )
            
            # Add the skill to the user's profile
            user_profile.skills.add(skill)

            return redirect('manage_skills')  # Redirect to the same page to see the updated list of skills

    # For GET request, render the skills page
    skills = Skill.objects.filter(userprofile__user=request.user)
    return render(request, 'skills/manage_skills.html', {'skills': skills})

@login_required
def book_session(request, skill_id):


    # Handle the booking of a session for a skill
    skill = get_object_or_404(Skill, id=skill_id)

    if request.method == 'POST':
        session_details = request.POST.get('session_details')
        if session_details:
            Booking.objects.create(user=request.user, skill=skill, session_details=session_details)
            messages.success(request, "Session booked successfully!")
            return redirect('manage_skills')
        else:
            messages.error(request, "Session details are required!")

    return render(request, 'skills/book_session.html', {'skill': skill})


# @login_required
# def complete_session(request, session_id):
#     # Assuming 'Session' is a model representing a user's session
#     session = get_object_or_404(Session, id=session_id)
#     if session.user == request.user:
#         # Award points after completing the session
#         user_profile = UserProfile.objects.get(user=request.user)
#         user_profile.points += 20  # Add 20 points for completing the session
#         user_profile.save()

#         # Optionally, mark the session as completed
#         session.completed = True
#         session.save()

#     return redirect('session_complete')  # Redirect to a page showing the session is completed



@login_required
def buy_points(request):
    if request.method == 'POST':
        points_to_buy = int(request.POST.get('points'))
        
        # Simulate a point purchase, assuming 1 point = 1 USD or any other conversion rate
        user_profile = UserProfile.objects.get(user=request.user)
        user_profile.points += points_to_buy
        user_profile.save()

        # Optionally, you could charge the user through a payment provider here
        
        return redirect('profile')  # Redirect to the user profile or wherever appropriate
    
    return render(request, 'buy_points.html')  # Render a form to allow users to buy points



@login_required
def delete_skill(request, id):
    skill = get_object_or_404(Skill, id=id)
    skill.delete()  # Delete the skill
    return redirect('profile')  # Redirect to the profile after deletion

@login_required
def update_skill(request, id):
    skill = get_object_or_404(Skill, id=id)
    
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()  # Save the updated skill
            return redirect('profile')  # Redirect to the profile page
    else:
        form = SkillForm(instance=skill)
    
    return render(request, 'update_skill.html', {'form': form, 'skill': skill})



@login_required
def add_skill(request):
    if request.method == "POST":
        skill_name = request.POST.get("skill_name")
        skill_description = request.POST.get("skill_description")
        
        # Check if skill already exists, otherwise create it
        skill, created = Skill.objects.get_or_create(
            name=skill_name,
            description=skill_description
        )
        
        # Add skill to user's profile
        user_profile = request.user.userprofile
        user_profile.skills.add(skill)
        user_profile.save()

        return redirect("profile")  # Redirect to the user's profile or another page

    return render(request, "users/add_skill.html")