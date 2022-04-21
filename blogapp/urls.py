from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('add-post', views.Addpost, name = 'Addpost')
]