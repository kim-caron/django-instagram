from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('create/', views.create, name='create'),
    path('<str:article_key>/', views.detail, name='detail'),
    path('<str:article_key>/update/', views.update, name='update'),
    path('<str:article_key>/delete/', views.delete, name='delete'),
    path('<str:article_key>/likes/', views.likes, name='likes'),
    path('<str:article_key>/save/', views.save, name='save'),
    path('<str:article_key>/create_comments/', views.create_comments, name='create_comments'),
    path('<str:article_key>/<int:comment_pk>/like_comments/', views.like_comments, name='like_comments'),
    path('<str:article_key>/<int:comment_pk>/delete_comments/', views.delete_comments, name='delete_comments'),
    path('<str:article_key>/<int:comment_pk>/create_subcomments/', views.create_subcomments, name='create_subcomments'),
]