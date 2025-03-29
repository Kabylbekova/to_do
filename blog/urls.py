
from django.urls import path
from .views import ViewBlog

urlpatterns = [
    path('api/', ViewBlog.as_view({'get':'list'}), name='blog-list'),
    
    
]