from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.posts),
    path('<int:pk>', views.posts),
    path('comment/<int:postId>', views.comments),
    path('reply/<int:pk>', views.replies),
    path('like/<int:id>', views.likes),
    path('disLike/<int:id>', views.disLikes),

]