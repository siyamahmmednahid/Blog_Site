from turtle import update
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# For Blogs
class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    blog_title = models.CharField(max_length=264, verbose_name='Blog Title')
    blog_slug = models.SlugField(max_length=264, unique=True, verbose_name='Blog Slug')
    blog_content = models.TextField(verbose_name='Blog Content')
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    blog_image = models.ImageField(upload_to='blog_images', blank=True, verbose_name='Blog Thumbnail')

    def __str__(self):
        return self.blog_title



# For Comments
class BlogComment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='blog_comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_comments')
    comment = models.TextField(verbose_name='Enter Comment')
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment



# For Likes
class BlogLike(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='blog_likes')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_likes')
    like_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username
