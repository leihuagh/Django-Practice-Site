from django.shortcuts import render


def index(request):
    context = {
        "title": "Welcome",
        "header": "Home Index"
    }
    return render(request, 'index.html', context)


def about(request):
    context = {
        "title": "About Us",
        "header": "About Us"
    }
    return render(request, 'index.html', context)


def contact(request):
    context = {
        "title": "Contact Us",
        "header": "Contact Us"
    }
    return render(request, 'index.html', context)
