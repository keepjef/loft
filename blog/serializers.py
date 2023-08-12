from rest_framework import serializers

from blog.models import Post, Theme


class ThemeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Theme
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):

    themes = ThemeSerializer(read_only=True, many=True)
    class Meta:
        model = Post

        fields = ('title', 'image_header', 'text', 'created', 'modified', 'is_draft', 'slug', 'themes')


