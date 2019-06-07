from django.urls import path
from blog.views import ProgrammingBlogPosts, WebDevelopmentBlogPosts, DataScienceAIBlogPosts, GeneralBlogPosts


urlpatterns = [
    path('posts/programming', ProgrammingBlogPosts.as_view()),
    path('posts/webdevelopment', WebDevelopmentBlogPosts.as_view()),
    path('posts/datascienceai', DataScienceAIBlogPosts.as_view()),
    path('posts/general', GeneralBlogPosts.as_view()),
]