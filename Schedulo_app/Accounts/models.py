from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    SECTIONS = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ]
    YEAR = [
        (1, '1st Year'),
        (2, '2nd Year'),
        (3, '3rd Year'),
        (4, '4th Year'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_number = models.IntegerField(unique=True)
    year = models.IntegerField(choices=YEAR)
    branch = models.CharField(max_length=50)
    sec = models.CharField(max_length=1, choices=SECTIONS)

class Teacher(models.Model):
    POSITION_CHOICES = [
        ('Head of Department', 'Head of Department'),
        ('Professor', 'Professor'),
        ('Associate Professor', 'Associate Professor'),
        ('Assistant Professor', 'Assistant Professor'),
        ('Lecturer', 'Lecturer'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    position = models.CharField(max_length=50, choices=POSITION_CHOICES)

