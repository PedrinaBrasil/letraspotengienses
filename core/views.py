from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
   return render(request, 'home.html')

def gallery(request):
    return render(request, 'gallery.html')

def lib(request):
    return render(request, 'acervo.html')

def about(request):
    return render(request, 'about.html')
