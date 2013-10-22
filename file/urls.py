from django.conf.urls.defaults import patterns, url
from file import views

urlpatterns = patterns('',
    url(r'^home/', views.home, name='home'),
    url(r'^about/', views.about, name='about'),
    url(r'^add_file/', views.add_file, name='add_file'),
)
