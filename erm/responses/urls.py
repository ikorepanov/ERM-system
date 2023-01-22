from django.urls import path
from . import views

app_name = 'responses'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('response/<int:pk>/', views.response_info, name='response_info'),
]
