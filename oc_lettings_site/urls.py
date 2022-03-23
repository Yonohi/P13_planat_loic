from django.contrib import admin
from django.urls import path, include
from lettings import urls as lettings_urls
from profiles import urls as profiles_urls
from . import views

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('sentry-debug/', trigger_error),
    path('', views.index, name='index'),
    path('lettings/', include(lettings_urls)),
    path('profiles/', include(profiles_urls)),
    path('admin/', admin.site.urls),
]
