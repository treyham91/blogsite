from django.urls import path
from blog.views import ProgrammingBlogPosts, WebDevelopmentBlogPosts, DataScienceAIBlogPosts, GeneralBlogPosts


urlpatterns = [
    path('posts/programming', ProgrammingBlogPosts.as_view(), name='programming'),
    path('posts/webdevelopment', WebDevelopmentBlogPosts.as_view(), name='web'),
    path('posts/datascienceai', DataScienceAIBlogPosts.as_view(), name='data'),
    path('posts/general', GeneralBlogPosts.as_view(), name='general'),
]