from django.urls import path
# Импортируем созданное нами представление
from .views import *


urlpatterns = [
   path('', PostsList.as_view(), name = 'posts_list'),
   path('search/', PostsSearch.as_view()),
   # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   path('<int:pk>', PostDetail.as_view(), name = 'post_detail'),
   path('create/', NewsCreate.as_view(), name='news_create'),
   path('<int:pk>/edit/', NewsEdit.as_view(), name='news_edit'),
   path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
]