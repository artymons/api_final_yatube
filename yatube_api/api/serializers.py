from rest_framework import serializers
import base64
from django.core.files.base import ContentFile
from posts.models import Comment, Group, Post, Follow, User


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        return super().to_internal_value(data)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')
    post = serializers.SlugRelatedField(read_only=True,
                                        slug_field='pk')

    class Meta:
        model = Comment
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')
    image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        model = Post
        fields = ('__all__')


class FollowSerializer(serializers.ModelSerializer):
    user = (
        serializers.SlugRelatedField(
            queryset=User.objects.all(),
            default=serializers.CurrentUserDefault(),
            slug_field='username'
        )
    )
    following = (
        serializers.SlugRelatedField(
            queryset=User.objects.all(),
            slug_field='username'
        )
    )

    class Meta:
        fields = '__all__'
        model = Follow
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['user', 'following'],
                message='Вы уже подписаны'
            )
        ]

    def validate(self, data):
        if data['user'] == data['following']:
            raise serializers.ValidationError(
                'Нельзя подписаться на себя'
            )
        return data
