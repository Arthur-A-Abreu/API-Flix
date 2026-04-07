
from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from genres.views import GenreCreateListView, GenreDetailView
from actors.views import ActorCreateListView, ActorDetailView 

urlpatterns = [
    path('admin/', admin.site.urls),
    # Genre URLs
    path('genres/', GenreCreateListView.as_view(), name='genre-create'),
    path('genres/<int:pk>/', GenreDetailView.as_view(), name='genre-detail'),
    # Actor URLs
    path('actors/', ActorCreateListView.as_view(), name='actor-create'),
    path('actors/<int:pk>/', ActorDetailView.as_view(), name='actor-detail'),
]
