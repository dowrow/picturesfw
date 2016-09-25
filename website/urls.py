from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.staticfiles import views as staticviews

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^upload$', views.upload, name='upload'),
    url(r'^success/(?P<last_picture_pk>.*)$', views.success, name='success'),
    url(r'^rules$', views.rules, name='rules'),
    url(r'^error$', views.error, name='error'),
    url(r'^gallery$', views.gallery, name='gallery'),
    url(r'^report/$', views.report, name='report'),
    url(r'^laughing/$', views.laughing, name='laughing'),
    url(r'^fearful/$', views.fearful, name='fearful'),
    url(r'^banana/$', views.banana, name='banana'),
    url(r'^media/(?P<path>.*)$', staticviews.serve,name='media'),
    url(r'^google37c1329649703458[\w.]html$', views.google, name='google'),
] + [url(r'^.*', views.error, name='error'),]