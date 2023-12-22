from django.shortcuts import get_object_or_404, render, redirect

from erm.settings import NUMBER_OF_RESULT_ENTRIES

from .models import Response

# from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required

from django.views.generic.edit import CreateView
from .forms import ResponseForm

from django.urls import reverse_lazy


def index(request):
    # responses = Response.objects.all()[:NUMBER_OF_RESULT_ENTRIES]
    title = 'Ваши отклики'
    context = {
        'title': title,
        # 'responses': responses,
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
    title = 'Об авторе проекта'
    context = {
        'title': title,
    }
    return render(request, 'responses/about.html', context)


def contact(request):
    title = 'Контакты'
    context = {
        'title': title,
    }
    return render(request, 'responses/contact.html', context)


# @login_required
# def application_list(request):
#     applications = JobApplication.objects.filter(user=request.user)
#     return render(request, 'responses/application_list.html', {'applications': applications})


# @login_required
# def create_application(request):
#     if request.method == 'POST':
#         form = JobApplicationForm(request.POST, request.FILES)
#         if form.is_valid():
#             application = form.save(commit=False)
#             application.user = request.user
#             application.save()
#             return redirect('application_list')
#     else:
#         form = JobApplicationForm()
#     return render(request, 'responses/create_application.html', {'form': form})


@login_required
def response_list(request):
    title = 'Мои отклики'
    responses = (Response.objects.prefetch_related('user',
                                                   'employer',
                                                   'agency',
                                                   'contacts')
                                 .all())
                                #  .order_by('-date')[:2])
                                #  .order_by('-date'))
    context = {
        'title': title,
        'responses': responses,
    }
    return render(request, 'responses/response_list.html', context)


@login_required
def response_detail(request, pk):
    title = f'Отклик №{pk}'
    response = get_object_or_404(Response, pk=pk)
    context = {
        'title': title,
        'response': response,
    }
    return render(request, 'responses/response_detail.html', context)


# @login_required
# def create_response(request):
#     title = 'Создать отклик'
#     context = {
#         'title': title,
#     }
#     return render(request, 'responses/create_response.html', context)


class ResponseView(CreateView):
    form_class = ResponseForm
    template_name = 'responses/create_response.html'
    success_url = reverse_lazy('responses:response_list')
