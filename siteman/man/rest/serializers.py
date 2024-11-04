from rest_framework import serializers
from man.models import Man


class ManSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Man
        fields = ('pk', 'title', 'content', 'cat', 'is_published', 'author')
