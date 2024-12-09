from django.urls import path, include
from .import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView


urlpatterns = [

    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(next_page='/profile/'), name='login'),  # Corrected login URL
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('skills/', views.skills, name='skills'),
    path('about/', views.about, name='about'),
    path('update-profile/', views.update_profile, name='update_profile'), 
    path('book_session/', views.book_session, name='book_session'),

    
]
