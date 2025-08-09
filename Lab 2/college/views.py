from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentRegistrationForm


def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(request, f"Student '{student.name}' registered successfully!")
            return redirect('register-student') 
    else:
        form = StudentRegistrationForm()

    return render(request, 'school/register_student.html', {'form': form})
