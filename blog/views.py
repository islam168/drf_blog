from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer


class PostListView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# class PostListView(ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class DetailView(RetrieveUpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


class CategoryListView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


    
