from django.shortcuts import render, redirect
from .models import Blog
from .forms import CreateBlog

# Create your views here.
def blogsView(request):
    data = Blog.objects.all()
    return render(request, 'blog/list.html', { 'blogs' : data })

def blogView(request, slug):
    blog = Blog.objects.get(id=slug)
    return render(request, 'blog/page.html', { 'blog' : blog })

def NewBlogView(request):
    form = CreateBlog()
    if request.method == "POST":
        form = CreateBlog(request.POST, request.FILES)
        if form.is_valid():
           form.save()
           return redirect('blog:list')
    return render(request, 'blog/new-blog.html', { 'form' : form })

def editView(request, slug):
    blog = Blog.objects.get(id=slug)
    if request.method == "POST":
        form = CreateBlog(request.POST, request.FILES, instance=blog)
        if form.is_valid():
           form.save()
           return redirect('blog:list')
    else:
        form = CreateBlog(instance=blog)
    return render(request, 'blog/new-blog.html', { 'form' : form })

def deleteView(request, slug):
    if request.method == "POST":
        blog = Blog.objects.get(id=slug)
        blog.delete()
        return redirect('blog:list')