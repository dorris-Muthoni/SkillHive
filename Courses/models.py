# courses/models.py
from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    """Represents a course."""
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    instructor = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Content(models.Model):
    """Represents course content or materials."""
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='course_materials/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.course.title}"
