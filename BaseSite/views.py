from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'website/index.html')


def explore(request):
    return render(request, 'website/explore.html')


def details(request):
    return render(request, 'website/details.html')


def create(request):
    return render(request, 'website/create.html')


def author(request):
    return render(request, 'website/author.html')
