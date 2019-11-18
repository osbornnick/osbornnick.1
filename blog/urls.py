from django.urls import path
from . import views


urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("<str:slug>/", views.blog_post, name="blog_post"),
    path("<category>/", views.blog_category, name="blog_category")
]
