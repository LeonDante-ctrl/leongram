from django.shortcuts import render
from .models import Post 
from django.http import HttpResponse
from django.views.generic import (
    ListView
)

class PostListView(ListView):
    template_name = 'pages/postlist.html'
    queryset = Post.objects.all()
    context_object_name = 'posts'
