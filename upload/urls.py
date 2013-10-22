from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^file/', include('file.urls', namespace="file")),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


