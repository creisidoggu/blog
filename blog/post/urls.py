from django.urls import path
from post import views

urlpatterns = [
    path('', views.post),
    path('list/', views.list_post, name='post_list'),
]
