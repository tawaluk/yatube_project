
from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    # Добавим в начало столбец pk
    list_display = ('pk', 'text', 'pub_date', 'author') 
    search_fields = ('text',) 
    list_filter = ('pub_date',)  

# При регистрации модели Post источником конфигурации для неё назначаем
# класс PostAdmin
admin.site.register(Post, PostAdmin) 
