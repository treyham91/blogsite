from django.db import models
from django.contrib.auth.models import User


class BlogUser(User):
    pass


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


class BlogComment(models.Model):
    post = models.ForeignKey('BlogPost', on_delete=models.CASCADE)
    comment_body = models.TextField(max_length=500)
    comment_date = models.DateTimeField(auto_now=True)


class BlogLike(models.Model):
    post = models.ForeignKey('BlogPost', on_delete=models.CASCADE)
    user = models.ForeignKey('BlogUser', on_delete=models.CASCADE)





