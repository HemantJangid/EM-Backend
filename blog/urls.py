from django.conf.urls import url
from .views.v1.blog import BlogListView

urlpatterns = [
    url(r'^v1/blog/list$', BlogListView.as_view()),
    # url(r'^v1/blog/(?P<blog_id>[\w\-]+)/detail$', BlogDetailView.as_view()),
]
