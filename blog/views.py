from .models import Blog
from rest_framework import viewsets
from .serializers import BlogSerializers 

class ViewBlog(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers
    
    
