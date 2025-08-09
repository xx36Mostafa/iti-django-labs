from django.shortcuts import render

# Create your views here.
def profile(request):
    context = {
        'name': 'Mostafa Nasser Anwar',
        'bio': 'Ai Student and Web Scraper With 4+ Years of Experience',
        'skills': ['Python', 'Django', 'HTML', 'CSS', 'JavaScript'],
    }
    return render(request, 'profile.html', context)
