from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('p/<int:article_pk>/', views.article_detail_update_delete, name='article_detail_update_delete'),
    path('likes/<int:article_pk>/like/', views.article_like, name='article_like'),
    path('save/<int:article_pk>/save/', views.article_save, name='article_save'),
    path('comments/<int:article_pk>/', views.comment_create_list, name='comment_create_list'),
    path('comments/<int:article_pk>/<int:comment_pk>/', views.comment_subcreate_detail_update_delete, name='comment_subcreate_detail_update_delete'),
    path('comments/like/<int:comment_pk>/', views.comment_like, name='comment_like'),
]