from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm, StudentForm, TeacherForm
from django.contrib.auth.decorators import login_required

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('choose_role')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def home(request):
    return render(request, 'Schedulo/index.html')

def choose_role(request):
    return render(request, 'accounts/choose_role.html')

def student_details(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = request.user
            student.save()
            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'accounts/student_details.html', {'form': form})

def teacher_details(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            teacher = form.save(commit=False)
            teacher.user = request.user
            teacher.save()
            return redirect('home')
    else:
        form = TeacherForm()
        
    return render(request, 'accounts/teacher_details.html', {'form': form})