from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def list_posts(request):
    return render(request, 'posts/list_posts.html')
def posts(request):
    return render(request, 'posts/posts.html')