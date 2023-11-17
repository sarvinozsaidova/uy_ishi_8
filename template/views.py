from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def main(request):
    posts = Post.objects.all()
    return render(request, 'analytics.html', {'posts':posts})
