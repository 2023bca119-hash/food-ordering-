from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'cafeteria/index.html')

def about(request):
    return render(request, 'cafeteria/about.html')