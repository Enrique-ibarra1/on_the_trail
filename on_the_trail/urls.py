from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('search_trail', views.search_trail),
    path('trail_profile/<int:trail_id>', views.trail_profile),
    path('favorite_trail', views.favorite_trail),
    path('user_profile/<int:user_id>', views.user_profile),

]