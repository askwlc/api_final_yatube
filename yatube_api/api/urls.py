from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router_v1 = routers.DefaultRouter()
router_v1.register('groups', GroupViewSet, basename='groups')
router_v1.register('posts', PostViewSet, basename='posts')
router_v1.register('follow', FollowViewSet, basename='follow')
router_v1.register(
    'posts/(?P<post_id>\\d+)/comments',
    CommentViewSet, basename='comments'
)

urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router_v1.urls)),
]
