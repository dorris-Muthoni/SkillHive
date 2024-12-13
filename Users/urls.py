from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(next_page='/profile/'), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),  # Update to use logout_user view
    path('profile/', views.profile, name='profile'),
    path('skills/', views.skills, name='skills'),  # Assuming you want the skills page to be at /skills/
    path('about/', views.about, name='about'),
    path('update-profile/', views.update_profile, name='update_profile'),
    path('book_session/', views.book_session, name='book session'),
    path('skills/manage/', views.manage_skills, name='manage_skills'),
    path('book_session/<int:skill_id>/', views.book_session, name='book_session'),
     path('skill/<int:id>/delete/', views.delete_skill, name='delete_skill'),  # URL to delete a skill
    path('skill/<int:id>/update/', views.update_skill, name='update_skill'),  # URL to update a skill
    path('add/', views.add_skill, name='add_skill'),  # URL to add a skill



]


    
    
