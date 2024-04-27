from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Article, Comment

@login_required
@api_view(['GET'])
def index(request):
    pass

@login_required
@api_view(['GET', 'POST'])
def create(request):
    pass

@api_view(['GET'])
def detail(request, article_key):
    pass

@login_required
@api_view(['GET', 'PUT'])
def update(request, article_key):
    pass

@login_required
@api_view(['DELETE'])
def delete(request, article_key):
    pass

@login_required
@api_view(['POST'])
def likes(request, article_key):
    pass

@login_required
@api_view(['POST'])
def save(request, article_key):
    pass

@login_required
@api_view(['POST'])
def create_comments(request, article_key):
    pass

@login_required
@api_view(['DELETE'])
def delete_comments(request, article_key, comment_pk):
    pass

@login_required
@api_view(['POST'])
def like_comments(request, article_key, comment_pk):
    pass

@login_required
@api_view(['POST'])
def create_subcomments(request, article_key, comment_pk):
    pass