from rest_framework import serializers
from core.models import Blog


class BlogDto(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ('uuid', 'blog_title', 'blog_description',
                  'blog_content', 'blog_image')
