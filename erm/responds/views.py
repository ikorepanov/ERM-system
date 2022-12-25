from django.shortcuts import get_object_or_404, render

from erm.settings import NUMBER_OF_RESULT_ENTRIES

from .models import Respond


def index(request):
    responds = Respond.objects.all()[:NUMBER_OF_RESULT_ENTRIES]
    template = 'responds/index.html'
    title = "Your responds for this moment"
    context = {
        'title': title,
        'responds': responds
    }
    return render(request, template, context)


def about(request):
    template = 'responds/about.html'
    return render(request, template)


def contact(request):
    template = 'responds/contact.html'
    return render(request, template)


def respond_info(request, pk):
    respond = get_object_or_404(Respond, pk=pk)
    template = 'responds/respond_info.html'
    title = f'Подробная инфа об отклике {pk}'
    context = {
        'title': title,
        'respond': respond,


    }
    return render(request, template, context)
