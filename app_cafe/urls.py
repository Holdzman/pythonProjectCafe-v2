from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from app_cafe.views import index_page

urlpatterns = [
    path("", index_page, name='index_page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)