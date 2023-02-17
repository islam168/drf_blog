from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'posts', PostListView)
router.register(r'categories', CategoryListView)

urlpatterns = [
    path('', include(router.urls)),
]
# urlpatterns = [
#     path('posts', PostListView.as_view({'get': 'list',
#                                         'post': 'create'}), name='post_list'),
#     path('posts/<int:pk>', PostListView.as_view({'get': 'retrieve',
#                                                  'put': 'update',
#                                                  'patch': 'partial_update',
#                                                  'delete': 'destroy'}), name='post_detail'),
#     path('categories/', CategoryListView.as_view({'get': 'list',
#                                                   'post': 'create'}), name='category_list'),
#     path('categories/<int:pk>', CategoryListView.as_view({'get': 'retrieve',
#                                                           'put': 'update',
#                                                           'patch': 'partial_update',
#                                                           'delete': 'destroy'}), name='category_list'),
