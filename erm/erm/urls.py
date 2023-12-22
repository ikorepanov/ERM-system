from django.contrib import admin
from django.urls import include, path
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('', include('responses.urls', namespace='responses')),
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls', namespace='users')),
    path('auth/', include('django.contrib.auth.urls')),
    # path('cv/')
]

# if settings.DEBUG:
#     urlpatterns += static(
#         settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
#     )
