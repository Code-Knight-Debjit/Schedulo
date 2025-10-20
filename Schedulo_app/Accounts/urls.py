from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('roles/', views.choose_role, name='choose_role'),
    path('student/details/', views.student_details, name='student_details'),
    path('teacher/details/', views.teacher_details, name='teacher_details'),
    # path('dashboard/', views.dashboard, name='dashboard'),
]
