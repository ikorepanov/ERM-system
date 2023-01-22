from django.shortcuts import get_object_or_404, render

from erm.settings import NUMBER_OF_RESULT_ENTRIES

from .models import Response


def index(request):
    responses = Response.objects.all()[:NUMBER_OF_RESULT_ENTRIES]
    template = 'responses/index.html'
    context = {
        'responses': responses
    }
    return render(request, template, context)


def about(request):
    template = 'responses/about.html'
    return render(request, template)


def contact(request):
    template = 'responses/contact.html'
    return render(request, template)


def response_info(request, pk):
    response = get_object_or_404(Response, pk=pk)
    template = 'responses/response_info.html'
    context = {
        'response': response,
    }
    return render(request, template, context)
