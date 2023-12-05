from django.shortcuts import get_object_or_404, render, redirect

from erm.settings import NUMBER_OF_RESULT_ENTRIES

from .models import Response
from .models import JobApplication
from .forms import JobApplicationForm

# from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required


def index(request):
    responses = Response.objects.all()[:NUMBER_OF_RESULT_ENTRIES]
    context = {
        'responses': responses
    }
    return render(request, 'responses/index.html', context)

# def paginator(request, responses):
#     paginator = Paginator(responses, NUMBER_OF_RESULT_ENTRIES)
#     page_number = request.GET.get('page')
#     return paginator.get_page(page_number)


# def index(request):
#     responses = Response.objects.all()
#     page_obj = paginator(request, responses)
#     context = {
#         'page_obj': page_obj,
#     }
#     return render(request, 'responses/index.html', context)


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


@login_required
def application_list(request):
    applications = JobApplication.objects.filter(user=request.user)
    return render(request, 'responses/application_list.html', {'applications': applications})


@login_required
def create_application(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()
            return redirect('application_list')
    else:
        form = JobApplicationForm()
    return render(request, 'responses/create_application.html', {'form': form})
