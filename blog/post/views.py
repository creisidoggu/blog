from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def list_post(request):
    return render(request, 'post/list_posts.html')
def post(request):
    return render(request, 'post/posts.html')