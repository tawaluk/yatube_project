from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Главная страница') # Возвращает на экран надпись

def group_posts(request, name_groop):
    return HttpResponse(f'Группа {name_groop}') # Вернет группа и слаг на экран