from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


class BlogUser(User):
    pass

    def __str__(self):
        return '%s %s email:%s' % self.first_name, self.last_name, self.email


class BlogPost(models.Model):
    PROGRAMMING = 'PRGR'
    WEB = 'WEB'
    DATA = 'DATA'
    GEN = 'GEN'
    topic_types = [
        (PROGRAMMING, 'Programming'),
        (WEB, 'Web Development'),
        (DATA, 'Data Science/Artificial Intelligence'),
        (GEN, 'General')
    ]
    topic_type = models.CharField(
        max_length=50,
        choices=topic_types,
        default=PROGRAMMING
    )
    title = models.CharField(max_length=50, default='Title')
    post_body = models.TextField(max_length=1000)
    date_posted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Topic:%s Title:%s Post:%s' % self.topic_type, self.title, self.post_body


class BlogComment(models.Model):
    post = models.ForeignKey('BlogPost', on_delete=models.CASCADE)
    comment_body = models.TextField(max_length=500)
    comment_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Post:%s Comment:%s Comment Date:%s' % self.post, self.comment_body, self.comment_date


class BlogLike(models.Model):
    post = models.ForeignKey('BlogPost', on_delete=models.CASCADE)
    user = models.ForeignKey('BlogUser', on_delete=models.CASCADE)

    def __str__(self):
        return 'Post:%s User:%s' % self.post, self.user


class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'topic_type', 'post_body']


class BlogSubscribeForm(ModelForm):
    class Meta:
        model = BlogUser
        fields = ['first_name', 'last_name', 'email']





