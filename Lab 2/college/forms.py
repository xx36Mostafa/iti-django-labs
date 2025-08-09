from django import forms
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        # يعني بنعرفه إن أحنا الفورم اللي جايلك دا هيكون تبع الموديل اللي هوا استيودنت و كمان دي الـ فيلدس اللي هتجيلك
        model = Student
        fields = ['name', 'email', 'course']
