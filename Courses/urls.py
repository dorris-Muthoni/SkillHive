from django.urls import path
from . import views 

urlpatterns =[
    path('', views.course_list, name='course_list'),
    path('<int:course_id>/', views.course_detail, name='course_detail'),
    path('<int:course_id>/content/', views.course_content, name='course_content'),
    path('<int:course_id>/certificate/', views.generate_certificate, name='generate_certificate'),
    
]