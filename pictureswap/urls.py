from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

"""
url(r'^', include('landing.urls')),
url(r'^beta/', include('website.urls')),
"""

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('website.urls')),
]



