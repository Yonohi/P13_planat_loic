from django.contrib import admin
from django.urls import path, include
from lettings import urls as lettings_urls
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include(lettings_urls)),
    path('profiles/', views.profiles_index, name='profiles_index'),
    path('profiles/<str:username>/', views.profile, name='profile'),
    path('admin/', admin.site.urls),
]
