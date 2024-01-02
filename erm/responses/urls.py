from django.urls import path

from .views import (about, contact, index,
                    response_detail, response_list)

from .views import ResponseView, EmployerView

app_name = 'responses'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('responses/', response_list, name='response_list'),
    path('responses/<int:pk>/', response_detail, name='response_detail'),  # возможно, изменить на <int:response_id>
    path('responses/create/', ResponseView.as_view(), name='create_response'),
    path('responses/some/', EmployerView.as_view(), name='create_employer'),
]
