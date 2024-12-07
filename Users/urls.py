from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('', include('Users.urls')), 
    path('register/',views.register, name='register'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('profile/',views.profile, name='profile'),
    path('skills/', views.skills, name='skills'),
    path('about/', views.about, name='about'),
    

]