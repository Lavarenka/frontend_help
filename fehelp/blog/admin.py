from django.contrib import admin
from .models import *

from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')  # поля для отображения в админке
    list_display_links = ('id', 'title')  # наименования которые будут ссылкой в админ
    search_fields = ('title',)  # поиск по полям
    prepopulated_fields = {"slug": ("title",)}


class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')  # поля для отображения в админке
    list_display_links = ('id', 'title')  # наименования которые будут ссылкой в админ
    search_fields = ('title',)  # поиск по полям
    prepopulated_fields = {"slug": ("title",)}


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','category', 'created_at', 'views', 'is_published')  # поля для отображения в админке
    list_display_links = ('id', 'title')  # наименования которые будут ссылкой в админ
    save_on_top = True # кнопки сверху в админке
    save_as = True # для добавления статей тестовых
    search_fields = ('title', 'content')  # поиск по полям
    list_editable = ('is_published',) # редактирование прямо из списка
    list_filter = ('is_published', 'category') # фильтр в админке
    readonly_fields = ('views', 'created_at')
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagsAdmin)
admin.site.register(Post, PostAdmin)

