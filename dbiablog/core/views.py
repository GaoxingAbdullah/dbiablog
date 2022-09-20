from django.shortcuts import render
from blog.models import Post

def homepage(request):
    posts = Post.objects.filter(status = Post.ACTIVE)
    return render(request, 'core/home.html', {'posts': posts})

def aboutpage(request):
    return render(request, 'core/about.html')

def featurepage(request):
    return render(request, 'core/feature.html')

def servicepage(request):
    return render(request, 'core/service.html')


