from django.shortcuts import render

def games_posts_views(request):
    return render(request,'catalogo.html')