from pyexpat import model
from turtle import pos
from django.http import HttpResponse, HttpResponseBadRequest
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

def post(request, pk):
    post = Post.objects.get(id = pk)
    return render(request, 'post.html', {'post':post})

@csrf_exempt
def Deletepost(request, pk):
    try:
        post = Post.objects.get(id = pk)
        post.delete()
        return HttpResponse("successfully deleted!")
    except Post.DoesNotExist:
        return HttpResponseBadRequest("Object does not exist")



