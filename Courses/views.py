
from django.shortcuts import render, get_object_or_404
from .models import Course, Content

def course_list(request):
    """List all available courses."""
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, course_id):
    """Display course details."""
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'courses/course_detail.html', {'course': course})

def course_content(request, course_id):
    """Provide access to course materials."""
    course = get_object_or_404(Course, id=course_id)
    materials = Content.objects.filter(course=course)
    return render(request, 'courses/course_content.html', {'course': course, 'materials': materials})

def generate_certificate(request, course_id):
    """Generate a certificate upon course completion."""
    # Logic for certificate generation
    return render(request, 'courses/certificate.html', {'course_id': course_id})

