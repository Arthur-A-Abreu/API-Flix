from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.MovieCreateListView.as_view(), name='movie-list'),
    path('movies/<int:pk>/', views.MovieDetailListView.as_view(), name='movie-detail'),
]