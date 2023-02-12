from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('group/<slug:name_groop>/', views.group_posts)
] 