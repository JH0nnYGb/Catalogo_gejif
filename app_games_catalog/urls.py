from django.urls import path
from app_games_catalog.views import games_posts_views

app_name = 'app_games_catalog'
 
urlpatterns = [
    path('',games_posts_views,name='games_posts'),
    path('Catalogo/',games_posts_views,name='games_posts'),
]

