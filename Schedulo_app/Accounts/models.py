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
    BRANCH = [
        ('CSE', 'Computer Science and Engineering'),
        ('ECE', 'Electronics and Communication Engineering'),
        ('ME', 'Mechanical Engineering'),
        ('CE', 'Civil Engineering'),
        ('EE', 'Electrical Engineering'),
        ('AIML', 'Artificial Intelligence and Machine Learning'),
        ('CSDS', 'Computer Science & Data Science'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_number = models.IntegerField(unique=True)
    year = models.IntegerField(choices=YEAR)
    branch = models.CharField(max_length=50, choices=BRANCH)
    sec = models.CharField(max_length=1, choices=SECTIONS)

    def __str__(self):
        return f"{self.user.username} - {self.roll_number}"

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

    def __str__(self):
        return f"{self.user.username} - {self.position}"
    
class Club(models.Model):
    POSITIONS = [
        ('President', 'President'),
        ('Vice President', 'Vice President'),
        ('Secretary', 'Secretary'),
        ('Member', 'Member'),
    ]
    user = models.ManyToManyField(User)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class StudentClubMembership(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    position = models.CharField(max_length=50, choices=Club.POSITIONS)

    def __str__(self):
        return f"{self.student.user.username} - {self.club.name} - {self.position}"
    
class TeacherClubAdvisory(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.teacher.user.username} - {self.club.name}"


class Event(models.Model):
    STATUS_CHOICES = [
        ('Upcoming', 'Upcoming'),
        ('Live', 'Live'),
        ('Completed', 'Completed'),
    ]
    MODE_CHOICES = [
        ('Online', 'Online'),
        ('Offline', 'Offline'),
        ('Hybrid', 'Hybrid'),
    ]
    VISISBILITY_CHOICES = [
        ('Public', 'Public'),
        ('Private', 'Private'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    mode = models.CharField(max_length=50, choices=MODE_CHOICES)
    visibility = models.CharField(max_length=50, choices=VISISBILITY_CHOICES)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.club.name}"

class EventRegistration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.user.username} - {self.event.title}"
    
class Reports(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Subject = models.CharField(max_length=100)
    CGPA = models.FloatField(max_length=4)

    def __str__(self):
        return f"Report for {self.student.user.username} - {self.Subject}"
    
class Tasks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending')

    def __str__(self):
        return f"Task: {self.title} for {self.teacher.user.username}"

