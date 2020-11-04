from django.shortcuts import render,get_object_or_404
from .models import Blog_Content
def blogs(req):
    x=Blog_Content.objects.all()
    return render(req, 'blog_home.html', {'awe':x})


def details(req,blog_id):
    blog=get_object_or_404(Blog_Content,pk=blog_id)
    return render(req,'blog_detail.html',{'blog_obj':blog,'id':blog_id})