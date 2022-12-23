from django.shortcuts import render


def index(request):
    template = 'responds/index.html'
    return render(request, template)


def about(request):
    template = 'responds/about.html'
    return render(request, template)


def contact(request):
    template = 'responds/contact.html'
    return render(request, template)
