from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from blog.models import BlogPost


class Home(ListView):
    context_object_name = 'recent_posts'
    queryset = BlogPost.objects.filter(id__lte=5)
    template_name = 'index.html'


class ProgrammingBlogPosts(ListView):
    model = BlogPost
    queryset = BlogPost.objects.filter(topic_type='PROG')


class WebDevelopmentBlogPosts(ListView):
    model = BlogPost
    queryset = BlogPost.objects.filter(topic_type='WEB')


class DataScienceAIBlogPosts(ListView):
    model = BlogPost
    queryset = BlogPost.objects.filter(topic_type='DATA')


class GeneralBlogPosts(ListView):
    model = BlogPost
    queryset = BlogPost.objects.filter(topic_type='GEN')
