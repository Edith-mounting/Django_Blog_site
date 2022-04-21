from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts':posts})

@csrf_exempt
def Addpost(request):
    jsonData = JSONParser().parse(request)
    print(jsonData)
    newPost = Post()
    newPost.title = jsonData['title']
    newPost.body = jsonData['body']
    newPost.save()
    return HttpResponse("success")
