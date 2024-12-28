# views.py in your app
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')
