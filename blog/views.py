from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    posts = Post.objects
    return render(request, "blog/home.html",{'posts':posts})

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk = post_id)
    return render(request, 'blog/detail.html', {'post':post_detail})