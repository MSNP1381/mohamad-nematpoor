from django.shortcuts import render
from .models import porto
def HomePage(req):
    porto_objects=porto.objects.all()
    return render(req,'HOME.html',{'proto_objects':porto_objects})

# Create your views here.
