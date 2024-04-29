from django.shortcuts import render, redirect
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Article, Comment
from .serializers import ArticleSerializer, ArticleDetailSerializer, ArticleListSerializer
from .serializers import CommentSerializer, CommentListSerializer

@api_view(['GET','POST'])
def article_create_list(request):
    if request.method == 'GET':
        User = get_user_model()
        person = User.objects.get(username=request.user)
        followings = person.followings.all()
        articles = Article.objects.filter(id__in=followings)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    else:
        serializer = ArticleSerializer(request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def article_detail_update_delete(request, article_pk):
    if request.method == 'GET':
        article = get_object_or_404(Article, key=article_pk)
        serializer = ArticleDetailSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        article = get_object_or_404(Article, key=article_pk)
        serializer = ArticleSerializer(article, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article)
            return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        article = get_object_or_404(Article, key=article_pk)
        article.delete()
        return Response({
            'message' : f'article : {article.pk} is deleted'
        }, status=status.HTTP_204_NO_CONTENT)


@login_required
@api_view(['POST'])
def article_like(request, article_pk):
    article = get_object_or_404(Article, key=article_pk)
    if article.like_users.filter(pk=request.user.pk).exists():
        article.like_users.remove(request.user)
        is_liked = False
    else:
        article.like_users.add(request.user)
        is_liked = True
    return Response({
        'is_liked' : is_liked
    }, status=status.HTTP_200_OK)


@login_required
@api_view(['POST'])
def article_save(request, article_pk):
    article = get_object_or_404(Article, key=article_pk)
    if article.save_users.filter(pk=request.user.pk).exists():
        article.save_users.remove(request.user)
        is_saved = False
    else:
        article.save_users.add(request.user)
        is_saved = True
    return Response({
        'is_saved' : is_saved
    }, status=status.HTTP_200_OK)

@login_required
@api_view(['GET','POST'])
def comment_create_list(request, article_pk):
    pass

@login_required
@api_view(['GET','POST','PUT','DELETE'])
def comment_subcreate_detail_update_delete(request, article_pk, comment_pk):
    pass

@login_required
@api_view(['POST'])
def comment_like(request, article_pk, comment_pk):
    pass