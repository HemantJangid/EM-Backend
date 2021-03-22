from rest_framework.views import APIView
from core.models import Blog
from middleware.response import success
from blog.serializer.dto import BlogDto


class BlogListView(APIView):
    def get(self, request):
        blogs = Blog.objects.order_by('blog_title').all()
        payload = {
            'blogs': BlogDto(blogs, many=True).data
        }
        return success(payload, 'blogs fetched successfully', True)
