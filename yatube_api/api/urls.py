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
jwt_urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]

urlpatterns = [
    path('v1/', include(jwt_urlpatterns)),
    path('v1/', include(router_v1.urls)),
]
