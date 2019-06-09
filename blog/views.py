from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView
from blog.models import BlogPost, BlogPostForm


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


def blog_post_form(request):
    form = BlogPostForm()
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request, 'post_success.html', {})
        else:
            print('FORM ERROR')

    return render(request, 'blog_post_form.html', {'form': form})


class Home(ListView):
    context_object_name = 'recent_posts'
    queryset = BlogPost.objects.filter(id__lte=5)
    template_name = 'home.html'


class ProgrammingBlogPosts(ListView):
    context_object_name = 'prog_posts'
    queryset = BlogPost.objects.filter(topic_type='PRGR')
    template_name = 'programming.html'


class WebDevelopmentBlogPosts(ListView):
    context_object_name = 'web_posts'
    queryset = BlogPost.objects.filter(topic_type='WEB')
    template_name = 'web.html'


class DataScienceAIBlogPosts(ListView):
    context_object_name = 'data_posts'
    queryset = BlogPost.objects.filter(topic_type='DATA')
    template_name = 'data_ai.html'


class GeneralBlogPosts(ListView):
    context_object_name = 'gen_posts'
    queryset = BlogPost.objects.filter(topic_type='GEN')
    template_name = 'general.html'
