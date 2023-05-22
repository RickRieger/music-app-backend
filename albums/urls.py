from django.urls import path, include
from albums import views



urlpatterns = [
    path('', views.user_albums),
    path('<int:pk>', views.user_albums),

]
