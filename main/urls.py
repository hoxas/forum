from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<str:category_name>/', views.category, name='category'),
    path('category/<str:category_name>/<int:post_id>/', views.post, name='post'),
]
