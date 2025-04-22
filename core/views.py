from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request):
    context = {
        'user' : request.user
    }
    return render(request,'core/home.html',context)

def about_view(request):
    return HttpResponse("<h1>About Us</h1><p>This is the about page.</p>")