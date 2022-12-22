from django.shortcuts import render


def index(request):
    template = 'responds/index.html'
    return render(request, template)
