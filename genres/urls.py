from django.urls import path
from . import views

urlpatterns = [
    path('genre/', views.GenreCreateListView.as_view(), name='genre-create'),
    path('genre/<int:pk>/', views.GenreDetailListView.as_view(), name='genre-detail'),
    ]