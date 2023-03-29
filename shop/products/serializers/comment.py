from rest_framework import serializers
from products.models import Comment
from user.serializers import UserInfoBriefSerializer


class CommentSerializer(serializers.ModelSerializer):

    user = UserInfoBriefSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'user', 'text')
