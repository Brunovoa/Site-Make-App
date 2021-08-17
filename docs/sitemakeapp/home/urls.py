from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = "home"

URLPatterns = [
    path("", views.PostListViews.as_view(), name="list"),
    path("<slug:slug>/", views.views.PostDetailView.as_view(), name="detail"),
]