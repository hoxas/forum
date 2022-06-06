from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_post/', views.create_post_POST, name='create_post'),
    path('category/<str:category_name>/', views.category, name='category'),
    path('category/<str:category_name>/<int:post_id>/', views.post, name='post'),
    path('category/<str:category_name>/<int:post_id>/create_comment/',
         views.create_comment_POST, name='create_comment'),
]
