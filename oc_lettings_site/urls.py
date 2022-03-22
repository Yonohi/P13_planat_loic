from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from lettings import urls as lettings_urls
from profiles import urls as profiles_urls
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include(lettings_urls)),
    path('profiles/', include(profiles_urls)),
    path('admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
