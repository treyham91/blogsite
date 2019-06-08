from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView
from blog.models import BlogPost


def search(request):
    if request.GET:
        post_search = request.GET['search']
        try:
            post = BlogPost.objects.filter(post_body__contains=post_search)
            return render(request, 'search_results.html', {'posts': post})
        except Http404:
            return "Couldn't load results"
    else:
        return render(request, 'search_results.html', {})


class Home(ListView):
    context_object_name = 'recent_posts'
    queryset = BlogPost.objects.filter(id__lte=5)
    template_name = 'home.html'


class ProgrammingBlogPosts(ListView):
    context_object_name = 'prog_posts'
    queryset = BlogPost.objects.filter(topic_type='PROG')
    # template_name = porgramming.html


class WebDevelopmentBlogPosts(ListView):
    context_object_name = 'web_posts'
    queryset = BlogPost.objects.filter(topic_type='WEB')
    # template_name = web.html


class DataScienceAIBlogPosts(ListView):
    context_object_name = 'data_posts'
    queryset = BlogPost.objects.filter(topic_type='DATA')
    # template_name = dataai.html


class GeneralBlogPosts(ListView):
    context_object_name = 'gen_posts'
    queryset = BlogPost.objects.filter(topic_type='GEN')
    # template_name = general.html
