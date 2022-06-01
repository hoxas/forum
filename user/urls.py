from django.urls import path

from . import views

urlpatterns = [
    path('', views.account, name='account'),
    path('auth/', views.auth, name='auth'),
    path('register/', views.register_POST, name='register'),
    path('login/', views.login_POST, name='login'),
    path('<str:profile_displayname>/', views.account, name='account-profile'),

]
