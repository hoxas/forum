from django.urls import path

from . import views

urlpatterns = [
    path('', views.account, name='account'),
    path('<str:profile_displayname>/', views.account, name='account-profile'),
]
