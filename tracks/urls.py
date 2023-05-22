from django.urls import path, include
from tracks import views



urlpatterns = [
    path('', views.user_tracks),
    path('<int:pk>', views.user_tracks),
]