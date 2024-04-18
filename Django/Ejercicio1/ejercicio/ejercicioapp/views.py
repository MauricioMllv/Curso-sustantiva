from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def proyecto1(request):
    return render(request, 'proyecto1.html')
def proyecto2(request):
    return render(request, 'proyecto2.html')
