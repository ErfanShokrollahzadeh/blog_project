from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='starting-page'),
    path('posts', views.posts, name='posts-page'),
    path('posts/<slug:slug>', views.single_post, name= 'post-detail-page') # toplearn.com/post/second-post
]
