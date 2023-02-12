from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    template = 'posts/index.html' # Путь до html приложения!
    title = 'Это главная страница проекта Yatube'
    context_title = {
        'title': title,
    }
    return render(request, template, context_title)

def group_posts(request, name_groop):
    template = 'posts/group_list.html'
    title = 'Здесь будет информация о группах проекта Yatube'
    context_title = {
        'title': title,
    }

    return render(request, template, context_title)