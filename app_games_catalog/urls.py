from django.urls import path
from app_games_catalog import games_posts_views

urlpatterns = [
    path('',games_posts_views,name='games_posts'),
    path('Catalogo/',games_posts_views,name='games_posts'),
]

