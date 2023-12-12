from django.urls import path

from .views import (about, application_detail, application_list, contact,
                    create_application, create_response, index,
                    response_detail, response_list)

from .views import ResponseView

app_name = 'responses'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('responses/', response_list, name='response_list'),
    path('responses/<int:pk>/', response_detail, name='response_detail'),  # возможно, изменить на <int:response_id>
    # path('responses/create/', create_response, name='create_response'),
    path('responses/create/', ResponseView.as_view(), name='create_response'),
    path('applications/', application_list, name='application_list'),
    path('applications/<int:pk>/', application_detail, name='application_detail'),
    path('applications/create/', create_application, name='create_application'),
]
