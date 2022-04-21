from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('add-post', views.Addpost, name = 'Addpost'),
    path('post/<str:pk>', views.post, name = "post"),
    path('delete-post/<str:pk>', views.Deletepost, name = "Deletepost")
]