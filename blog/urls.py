from django.urls import path
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('api/', include('blog.urls'))
    path('posts', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>', DetailView.as_view(), name='post_detail')
]