from django.http import HttpResponse
# from django.shortcuts import render


def index(request):
    html = '<h1> Какой-то заголовок </h1>'
    return HttpResponse(html)
