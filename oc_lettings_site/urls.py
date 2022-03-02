from django.contrib import admin
from django.urls import path, include
from lettings import urls as lettings_urls
from profiles import urls as profiles_urls
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include(lettings_urls)),
    path('profiles/', include(profiles_urls)),
    path('admin/', admin.site.urls),
]
