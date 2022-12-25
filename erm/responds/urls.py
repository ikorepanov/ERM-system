from django.urls import path
from . import views

app_name = 'responds'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('respond/<int:pk>/', views.respond_info, name='respond_info'),
]
