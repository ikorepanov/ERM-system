from django.urls import path
from .views import index, about, contact, response_info, application_list, create_application

app_name = 'responses'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('response/<int:pk>/', response_info, name='response_info'),
    path('applications/', application_list, name='application_list'),
    path('applications/create/', create_application, name='create_application'),
]
