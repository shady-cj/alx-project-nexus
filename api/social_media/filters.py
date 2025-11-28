from django_filters import rest_framework as filters
from .models import Bookmark, Follow, Follow, Post, Profile, Interaction



class PostFilter(filters.FilterSet):
    order_by = filters.OrderingFilter(
        fields=(
                ('created_at', 'created'),
                ('updated_at', 'modified'),
        )
    )
    class Meta:
        model = Post
        fields = {
            'author__username': ['exact', 'icontains'],
            'is_published': ['exact'],
            'created_at': ['exact', 'lt', 'gt'],
            'updated_at': ['exact', 'lt', 'gt'],
            'deleted': ['exact'],
        }

class ProfileFilter(filters.FilterSet):
    class Meta:
        model = Profile
        fields = {
            'first_name': ['exact', 'icontains', 'istartswith'],
            'last_name': ['exact', 'icontains', 'istartswith'],
            'user__username': ['exact', 'icontains'],
        }


class InteractionFilter(filters.FilterSet):
    class Meta:
        model = Interaction
        fields = {
            'type': ['exact'],
            'user__username': ['exact', 'icontains'],
            'post__id': ['exact'],
            'created_at': ['exact', 'lt', 'gt'],
        }

class FollowFilter(filters.FilterSet):
    order_by = filters.OrderingFilter(
        fields=( 
                ('created_at', 'followed_at'),
        )
    )
    class Meta:
        model = Follow
        fields = {
            'user__username': ['exact', 'icontains'],
            'followed_by__username': ['exact', 'icontains'],
            'created_at': ['exact', 'lt', 'gt'],
        }


class BookmarkFilter(filters.FilterSet):
    order_by = filters.OrderingFilter(
        fields=( 
                ('created_at', 'bookmarked_at'),
        )
    )
    class Meta:
        model = Bookmark
        fields = {
            'user__username': ['exact', 'icontains'],
            'post__id': ['exact'],
            'created_at': ['exact', 'lt', 'gt'],
        }