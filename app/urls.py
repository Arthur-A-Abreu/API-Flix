
from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from genres.views import GenreCreateListView, GenreDetailListView
from actors.views import ActorCreateListView, ActorDetailListView 
from movies.views import MovieCreateListView, MovieDetailListView
from reviews.views import ReviewCreateListView, ReviewDetailListView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Genre URLs
    path('genres/', GenreCreateListView.as_view(), name='genre-create'),
    path('genres/<int:pk>/', GenreDetailListView.as_view(), name='genre-detail'),
    # Actor URLs
    path('actors/', ActorCreateListView.as_view(), name='actor-create'),
    path('actors/<int:pk>/', ActorDetailListView.as_view(), name='actor-detail'),
    # Movie URLs
    path('movies/', MovieCreateListView.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieDetailListView.as_view(), name='movie-detail'),
    # Review URLs
    path('reviews/', ReviewCreateListView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetailListView.as_view(), name='review-detail'),
]
