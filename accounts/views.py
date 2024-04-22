from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import CustomUserChangeForm, CustomUserCreationForm
from rest_framework.decorators import api_view

# Create your views here.
def login(request):
    if request.user.is_authenticated():
        return redirect('articles:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, request.user)
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('accounts:login')

def signup(request):
    if request.user.is_authenticated():
        return redirect('articles:index')
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form
    }
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
    person = User.object.get(username=username)
    articles = person.article_set.all()
    stories = person.story_set.filter()
    highlights = person.highlights_set.all()
    followings = person.followings.all()
    followers = person.followers.all()
    save_articles = person.save_articles.all()
    tagged_articles = person.tagged_articles.all()
    context = {
        'person' : person,
        'articles' : articles,
        'stories' : stories,
        'highlights' : highlights,
        'followings' : followings,
        'followers' : followers,
        'save_articles' : save_articles,
        'tagged_articles' : tagged_articles,
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