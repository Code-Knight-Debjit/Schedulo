from django.contrib import admin
from .models import Student, Teacher, Club, StudentClubMembership, TeacherClubAdvisory, Event, Tasks, Reports, EventRegistration 


# Register your models here.

class ClubAdmin(admin.ModelAdmin):
    filter_horizontal = ('user',)

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Club, ClubAdmin)
admin.site.register(StudentClubMembership)
admin.site.register(TeacherClubAdvisory)
admin.site.register(Event)
admin.site.register(Tasks)
admin.site.register(Reports)
admin.site.register(EventRegistration)
