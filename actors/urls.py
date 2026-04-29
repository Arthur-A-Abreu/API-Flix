from django.urls import path
from . import views

urlpatterns = [
    path('actors/', views.ActorCreateListView.as_view(), name='actor-create'),
    path('actors/<int:pk>', views.ActorDetailListView.as_view(), name='actor-detail'),
]