from django.urls import path
from . import views
#prefix
app_name='post'

urlpatterns = [
    path('', views.posts, name='posts'),
    path('<slug:slug>', views.post_detail, name='detail'),
    path('new/post', views.new_post, name='new_post'),
    path('sobre', views.sobre, name='sobre'),
]
