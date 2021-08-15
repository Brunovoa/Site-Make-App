import django
from django.contrib.auth import models
from django.db.models.fields import DateTimeField
from django.shortcuts import render
from django.views.generic import DetaliView, ListView
from .models import Post

# Create your views here.

class PostListViews(ListView):
    model = Post

class PostDetailView(DetaliView):
    model = Post
