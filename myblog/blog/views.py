from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    template_name = "blog/post/list.html"


class PostDetailView(DetailView):
    queryset = Post.published.all()
    template_name = "blog/post/detail.html"