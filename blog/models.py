from django.db import models
from django.urls import reverse
from datetime import date
import uuid
from django.contrib.auth.models import User


# Create your models here.


class Blog(models.Model):

    name = models.CharField(max_length=200, help_text='Enter the name/title of the blog')
    description = models.TextField(max_length=2000, help_text='Write description/content of the blog here')
    author = models.ForeignKey('BlogAuthor', on_delete=models.SET_NULL, null=True)
    post_date = models.DateField(default=date.today)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])



class BlogAuthor(models.Model):

    name = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=1000, help_text='Write a brief bio about the author')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blogauthor-detail', args=[str(self.id)])



class BlogComment(models.Model):

    description = models.TextField(max_length=1000, help_text='Write your comment here')
    post_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True),
    blog = models.ForeignKey(Blog, on_delete=models.SET_NULL, null=True),

    def __str__(self):

        max_len = 75

        if len(self.description) > max_len:
            short_description = self.description[:max_len] + '...'
        else:
            short_description = self.description

        return short_description
