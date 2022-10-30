from django.db import models
from django.urls import reverse

'''
category
=============
title,slug

Tag
=============
title, slug

Post
=============
title, slug, mini_content, content, created_at, pfoto, views, category, tags
'''

class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование категории')
    slug = models.SlugField(max_length=255, verbose_name='url категории', unique=True) # для урла. уникален

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug}) # для ссылок

    class Meta:
        verbose_name = 'Категория'  # ед число
        verbose_name_plural = 'Категории'  # мн число
        ordering = ['id']  # sort

class Tag(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование тега')
    slug = models.SlugField(max_length=100, verbose_name='url тега', unique=True)  # для урла. уникален

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тег'  # ед число
        verbose_name_plural = 'Теги'  # мн число
        ordering = ['title']  # sort

class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(max_length=255, verbose_name='url', unique=True)  # для урла. уникален
    content = models.TextField(blank=True, verbose_name='Статья')
    mini_content = models.TextField(blank=True, verbose_name='Статья для заголовка')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    pfoto = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='медиа')
    views = models.IntegerField(default=0, verbose_name='Количестко просмотров')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True,related_name='posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={"slug": self.slug}) # для ссылок

    class Meta:
        verbose_name = 'Статья'  # ед число
        verbose_name_plural = 'Статьи'  # мн число
        ordering = ['-created_at']  # sort
