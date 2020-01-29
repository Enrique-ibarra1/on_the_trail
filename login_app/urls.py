from django.urls import path
from . import views
urlpatterns = [
    path('', views.index ),
    path('user/register', views.register),
    path('success', views.success),
    path('user/login', views.user_login),
    path('user/logout', views.user_logout),
]