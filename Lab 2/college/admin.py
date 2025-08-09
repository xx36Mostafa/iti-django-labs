from django.contrib import admin
from .models import Student, Course

# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'course')
    list_filter = ('course',)
    search_fields = ('name', 'email')
