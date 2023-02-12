from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('group/<slug:name_groop>/', views.group_posts, name='group_posts')
] 