from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('emailsignup/', views.signup, name='signup'),
    path('edit/',views.edit,name='edit'),
    path('delete/', views.delete,name='delete'),
]
