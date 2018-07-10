from django.shortcuts import render
from .models import Post
from django.db.models import Q
# Create your views here.
def post_list(request):
    post_list = Post.objects.all()

    q = request.GET.get('q','') #q 인자가 앖이 있으면 가져오고 없으면 '' 이다
    if q:
        qs = post_list.filter(title__icontains = q)
    else:
        qs = post_list




    return render(request, 'blog/post_list.html',{
            'post_list':qs,
            'q':q
    })
