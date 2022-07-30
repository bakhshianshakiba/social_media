import imp
from django.shortcuts import render
from .models import Post
from django.contrib import messages
# Create your views here.


def posts(request):
    if request.method == "POST":
        title = request.POST.get('title')
        body = request.POST.get('body')
        if title and body:
            p = Post.objects.create(title=title, body=body)
            p.save()
            messages.add_message(request, messages.SUCCESS,
                                 "you post hase saved successfully!")
        posts = Post.objects.all().order_by('-create_at')
        return render(request, 'blog/posts.html', {'posts': posts})

    elif request.method == 'GET':
        posts = Post.objects.all().order_by('-create_at')
        return render(request, 'blog/posts.html', {'posts': posts})
