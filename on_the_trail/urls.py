from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('search_trail', views.search_trail)
]