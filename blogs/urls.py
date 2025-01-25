"""Defines URL patterns for blogs."""

from django.urls import path

from . import views

app_name='blogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that lists all blogs.
    path('blogs/', views.blogs, name='blogs'),
    # Page that lists a specific blog and its posts.
    path('blogs/<int:blog_id>/', views.blog, name='blog'),
    # Page for creating a new blog.
    path('new_blog/', views.new_blog, name='new_blog'),
    # Page for creating a new post for a specific blog.
    path('new_post/<int:blog_id>/', views.new_post, name ='new_post'),
    # Page for editing an existing post.
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
]