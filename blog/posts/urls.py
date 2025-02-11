from django.urls import path
from posts import views

urlpatterns = [
    path('', views.posts),
    path('list/', views.list_posts, name='post_list'),
]
