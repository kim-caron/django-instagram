from django.shortcuts import render, redirect

def index(request):
    pass

def create(request):
    pass

def detail(request, article_key):
    pass

def update(request, article_key):
    pass

def delete(request, article_key):
    pass

def likes(request, article_key):
    pass

def save(request, article_key):
    pass

def create_comments(request, article_key):
    pass

def delete_comments(request, article_key, comment_pk):
    pass

def like_comments(request, article_key, comment_pk):
    pass

def create_subcomments(request, article_key, comment_pk):
    pass