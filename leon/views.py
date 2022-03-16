from datetime import timezone
from django.contrib.auth.models import User 
from django.shortcuts import render, get_object_or_404
from leon.forms import PostForm
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.urls import reverse 
from .models import Post 
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    RedirectView,
)

class PostListView(ListView):
    template_name = 'pages/postlist.html'
    queryset = Post.objects.all().filter(created_period__lte=timezone.now()).order_by('-created_period')
    context_object_name = 'posts'

class PostCreateView(CreateView):
    template_name = 'pages/post_create.html'
    form_class = PostForm
    queryset=Post.objects.all()
    #success_url = '/'
    
    def form_valid(self, form):
        print(form.cleaned_data)
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
class PostDetailView(DetailView):
    template_name = 'pages/post_detail.html'
    queryset = Post.objects.all().filter(created_period__lte=timezone.now())    
    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Post, id=id)
    
    
class PostUpdateView(UpdateView):
    template_name = 'pages/create.html'
    form_class = PostForm 

    def get_object(self):
     id_ = self.kwargs.get("id")
     return get_object_or_404(Post, id=id)

    def form_valid(self, form):
            form.instance.author = self.request.user 
            return super().form_valid(form) 

class PostDeleteView(DeleteView):
    template_name = 'pages/delete.html'

    def get_object(self):
        id_=self.kwargs.get("id")
        return get_object_or_404(Post, id=id)

    def get_success_url(self):
        return reverse('pages:post_list')  
      
 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    