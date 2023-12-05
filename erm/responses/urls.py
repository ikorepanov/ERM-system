from django.urls import path

from .views import (about, application_list, contact, create_application,
                    index, response_detail, response_info, response_list)

app_name = 'responses'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('response/<int:pk>/', response_info, name='response_info'),  # потом удалить за ненадобностью
    path('responses/', response_list),
    path('responses/<int:pk>', response_detail),  # возможно, изменить на <int:response_id>
    path('applications/', application_list, name='application_list'),
    # path('applications/<int:pk>/', application_detail, name='...'),
    path('applications/create/', create_application, name='create_application'),
]
