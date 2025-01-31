from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Blog, Post
from .forms import BlogForm, PostForm

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

@login_required
def new_blog(request):
    """Page for creating a new blog."""
    if request.method != 'POST':
        # No data submitted, create a blank form.
        form = BlogForm()
    else:
        # POST data submitted; process data.
        form = BlogForm(data = request.POST)
        if form.is_valid():
            new_blog= form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            return redirect('blogs:blogs')
    
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'blogs/new_blog.html',context)

@login_required
def new_post(request, blog_id):
    """Page for creating a new post for a specific blog."""
    blog = Blog.objects.get(id=blog_id)

    if blog.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # No data submitted, create a blank form.
        form = PostForm()
    else:
        # POST data submitted; process data.
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.blog = blog
            new_post.save()
            return redirect('blogs:blog', blog_id=blog_id)
        
    # Display a blank or invalid form.
    context = {'blog':blog, 'form': form}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, post_id):
    """Page for editing an existing post."""
    post = Post.objects.get(id=post_id)
    blog = post.blog

    if blog.owner != request.user:
        raise Http404


    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry
        form = PostForm(instance = post)

    else:
        # POST data submitted; process data.
        form = PostForm(instance=post, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog', blog_id = blog.id)

    context = {'post':post, 'blog':blog, 'form': form}
    return render(request, 'blogs/edit_post.html', context)
