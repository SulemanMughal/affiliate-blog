from django.db import models
from django.conf import settings
from embed_video.fields import EmbedVideoField
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField



class Category(models.Model):
    question   =       models.TextField()    
    description=       models.TextField()
    name       =       models.CharField(max_length=150)
    slug       =       models.CharField(max_length=150)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Category"

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category   =       models.ForeignKey(Category, on_delete = models.CASCADE)
    question   =       models.TextField()    
    description=       models.TextField()
    name       =       models.CharField(max_length=150)
    slug       =       models.CharField(max_length=150)
    image       =       models.ImageField(blank=True)


    class Meta:
        verbose_name = "Sub Category"
        verbose_name_plural = "Sub Category"


    def __str__(self):
        return self.name


class Blog(models.Model):
    author              =       models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category            =       models.ForeignKey(Category, on_delete = models.CASCADE)
    sub_category        =       models.ForeignKey(SubCategory, on_delete = models.CASCADE)
    title               =       models.CharField(max_length=1000)
    meta_description    =       models.CharField(max_length=1000)
    slug                =       models.CharField(max_length=1000)
    image               =       models.ImageField(blank=True)
    home_image          =       models.ImageField(blank=True)
    video               =       EmbedVideoField(blank=True)
    description         =       RichTextUploadingField()
    card_description    =       models.TextField()
    created_at          =       models.DateTimeField(auto_now_add=True)
    updated             =       models.DateTimeField(auto_now=True)
    publish             =       models.BooleanField(blank=True,default=False)
    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Blogs"
        verbose_name_plural = "Blogs"

    def __str__(self):
        return self.title

class PopularBlogs(models.Model):
    category    =       models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category=       models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    blog        =       models.ForeignKey(Blog, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Popular Blogs"
        verbose_name_plural = "Popular Blogs"

    def __str__(self):
        return self.blog.title

class HomeSectionBlogs(models.Model):

    blog        =       models.ForeignKey(Blog, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "HomeSection Blogs"
        verbose_name_plural = "HomeSection Blogs"

    def __str__(self):
        return self.blog.title

class BlogComment(models.Model):
    name        =       models.CharField(max_length=100)
    email       =       models.CharField(max_length=100)
    description =       models.TextField(max_length=1000)
    post_date   =       models.DateTimeField(auto_now_add=True)
    blog        =       models.ForeignKey(Blog, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-post_date"]

    def __str__(self):
        return self.description
    
  



class BlogReply(models.Model):
    name        =       models.CharField(max_length=100)
    email       =       models.CharField(max_length=100)
    description =       models.TextField(max_length=1000)
    post_date   =       models.DateTimeField(auto_now_add=True)
    comment     =       models.ForeignKey(BlogComment, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-post_date"]
        verbose_name_plural = "Blog Reply"

    def __str__(self):
        return self.name

    
# from django.contrib.sites.shortcuts import get_current_site
# from django.http import request

# from django.contrib.sites.models import Site


# class Category(models.Model):
#     Name      =       models.CharField(max_length=500)
#     slug      =       models.CharField(max_length=500)
#     def __str__(self):
#         return self.Name


# class BlogAuthor(models.Model):
#     author     =       models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
#     image      =       models.ImageField()
#     bio        =       models.TextField(help_text='Write something about you')

#     def __str__(self):
#         return self.author.username


# class Subscribe(models.Model):
#     name = models.CharField(max_length = 30)
#     email = models.EmailField()
#     date_added = models.DateField(auto_now_add=True)

#     class Meta:
#         verbose_name = "Subscribe"
#         verbose_name_plural = "Subscribers"

#     def __str__(self):
#             return self.email
    