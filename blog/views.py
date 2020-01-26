from django.shortcuts import render
from .models import Post
from django.utils import timezone

def post_list(request):
	posts = Post.objects.filter(published_date_lte=timezone.now()).order_by("publish_date")
	return render(request, "blog/post_list.html", {})
# Create your views here.
