from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('responses.urls', namespace='responses')),
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
]
