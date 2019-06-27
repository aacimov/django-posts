from django.conf.urls import url

from posts.views import PostDetail, PostList

urlpatterns = [
    url(r'^(?P<id>[\w-]+)/(?P<slug>[\w-]+)/', PostDetail.as_view(), name='post_detail'),
    url(r'^', PostList.as_view(), name='posts_list'),
]