from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('email-signup/', views.signup, name='signup'),
    path('edit/',views.edit,name='edit'),
    path('delete/', views.delete,name='delete'),
    path('<str:username>/', views.profile, name='profile'),
    path('<str:username>/follow/', views.follow, name='follow'),
]
