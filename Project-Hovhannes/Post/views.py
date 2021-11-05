from django.shortcuts import render, redirect
from .models import PostModel
from django.views.generic import ListView, TemplateView, DetailView, CreateView

class PostLists(ListView):
    model = PostModel
    template_name = 'Post/all_post.html'
    context_object_name = 'posts'

class Details(DetailView):
    model = PostModel
    context_object_name = 'Detail'

class PostCreate(CreateView):
    model = PostModel
    fields = ['image', 'Title', 'Description', 'Type', 'Area', 'Rooms', 'Address', 'telephone']

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return redirect('all-posts')
















