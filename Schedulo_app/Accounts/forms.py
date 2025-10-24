from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Student, Teacher, StudentClubMembership, Tasks

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['roll_number', 'year', 'branch', 'sec']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['subject', 'position']

class ClubMembershipForm(forms.ModelForm):
    class Meta:
        model = StudentClubMembership
        fields = ['student', 'club', 'position']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'description', 'teacher', 'due_date', 'status']

