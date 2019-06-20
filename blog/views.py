from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import logout, authenticate, login

from blog.models import BlogPost, BlogPostForm, BlogSubscribeForm, CreateUserForm, BlogComment
from .Forms.form import LoginForm


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


def blog_subscribe_form(request):
    subscribe_form = BlogSubscribeForm()
    if request.method == 'POST':
        subscribe_form = BlogSubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save(commit=True)
            return render(request, 'subscribe_success.html', {})
        else:
            raise Exception('Form Error')

    return render(request, 'blog_subscribe_form.html', {'subscribe_form': subscribe_form})


def create_new_user(request):
    user_creation_form = CreateUserForm()
    if request.POST:
        try:
            if user_creation_form.is_valid():
                user_creation_form.save(commit=True)
                return render(request, 'home.html', {})
            # else:
            #     print('FORM ERROR')
        except Exception as e:
            print(e)

    return render(request, 'user_creation_form.html', {'user_creation_form': user_creation_form})


def login_view(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return render(request, 'home.html', {})
            else:
                raise Exception('Username or Password is incorrect')

        return render(request, 'LoginForm.html', {'login_form': login_form})


def logout_view(request):
    logout(request)


class Home(TemplateView):
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['recent_posts'] = BlogPost.objects.filter(id__lte=5)
        context_data['comments'] = BlogComment.objects.filter(post_id=context_data['recent_posts'].post_id)
        return context_data

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
