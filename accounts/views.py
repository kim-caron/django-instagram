from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model, update_session_auth_hash, authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def login(request):
    if request.user.is_authenticated:
        context = {
            'message' : 'You are already logged in.'
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
    
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        auth_login(request, user)
        context = {
            'message' : 'Login successfully performed.'
        }
        return Response(context, status=status.HTTP_200_OK)
    else:
        context = {
            'message' : 'Invalid username or password.'
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
    
@login_required
@api_view(['POST'])
def logout(request):
    auth_logout(request)
    return Response({
        'message' : 'Login successfully performed.'
    }, status=status.HTTP_200_OK)

@api_view(['POST'])
def signup(request):
    if request.user.is_authenticated():
        context = {
            'message' : 'You are already logged in.'
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
    
    username = request.POST['username']
    password = request.POST['password']

    return render(request, 'accounts/signup.html', context)

@login_required
def edit(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/edit.html', context)

@login_required
def delete(request):
    request.user.delete()
    return redirect('accounts:login')

@login_required
def change_password(request, user_pk):
    t_user = get_user_model().objects.get(pk=user_pk)
    if t_user != request.user:
        return redirect('articles:index')
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form,
    }
    return render(request,'account/change_password.html',context)

def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    articles = person.article_set.all()
    # stories = person.story_set.filter()
    # highlights = person.highlights_set.all()
    followings = person.followings.all()
    followers = person.followers.all()
    context = {
        'person' : person,
        'articles' : articles,
        #'stories' : stories,
        #'highlights' : highlights,
        'followings' : followings,
        'followers' : followers,
    }
    return render(request, 'accounts/profile.html', context)

@login_required
def follow(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    if request.user != person:
        if person.followers.filter(pk=request.user.pk).exists():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)
    return redirect('accounts:profile', person.username)