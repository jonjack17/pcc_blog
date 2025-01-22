from django.shortcuts import render

from .models import Blog, Post

def index(request):
    """The home page for Blog."""
    return render(request, 'blogs/index.html')

def blogs(request):
    """Page that lists all blogs."""
    blogs = Blog.objects.order_by('date_added')
    context = {'blogs':blogs}
    return render(request, 'blogs/blogs.html', context)

def blog(request, blog_id):
    """Page that lists a specific blog and its posts."""
    blog = Blog.objects.get(id=blog_id)
    posts = blog.post_set.order_by('-date_added')
    context = {'blog':blog, 'posts':posts}
    return render(request, 'blogs/blog.html', context)