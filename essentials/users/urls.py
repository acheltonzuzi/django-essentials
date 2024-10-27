
from django.urls import path
from . import views

app_name='users'

urlpatterns = [
    path('', views.regiter, name='register'),
    path('login', views.entrar, name='login'),
    path('logout', views.sair, name='logout'),
]

