from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.
from . import forms
def posts(request):
    posts=Post.objects.all().order_by('-date')
    return render(request,'posts/index.html',{'posts':posts})

@login_required(login_url='users:login')
def new_post(request):
    if(request.method=='POST'):
        form=forms.PostForm(request.POST,request.FILES)
        if(form.is_valid()):
            newpost=form.save(commit=False)
            newpost.author=request.user
            newpost.save()
            return redirect('post:posts')
    else:
        form=forms.PostForm()
    return render(request,'posts/new_post.html',{'form':form})

def sobre(request):
    return render(request,'posts/sobre.html')

@login_required(login_url='users:login')
def post_detail(request,slug):
    post=Post.objects.get(slug=slug)
    return render(request,'posts/detail.html',{'post':post})
