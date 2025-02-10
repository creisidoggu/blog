from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return render(request, 'blog.html')
def main(request):
    return HttpResponse(f'{[number for number in range(20)]}')