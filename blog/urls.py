from django.urls import path
from blog.views import (
    ProgrammingBlogPosts,
    WebDevelopmentBlogPosts,
    DataScienceAIBlogPosts,
    GeneralBlogPosts,
    search,
    blog_post_form,
    blog_subscribe_form,
    login_view,
    logout_view,
    create_new_user
)


urlpatterns = [
    path('posts/programming', ProgrammingBlogPosts.as_view(), name='programming'),
    path('posts/webdevelopment', WebDevelopmentBlogPosts.as_view(), name='web'),
    path('posts/datascienceai', DataScienceAIBlogPosts.as_view(), name='data'),
    path('posts/general', GeneralBlogPosts.as_view(), name='general'),
    path('search/', search, name='search'),
    path('post/', blog_post_form, name='post_form'),
    path('subscribe/', blog_subscribe_form, name='subscribe_form'),
    path('login/', login_view, name='login_form'),
    path('logout/', logout_view, name='logout'),
    path('create/', create_new_user, name='create_user_form'),
]