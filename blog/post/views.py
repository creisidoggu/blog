from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def list_post(request):
    posts = Post.objects.all().order_by('date')
    return render(request, 'post/list_posts.html', 
                  {'posts': posts},
                  )