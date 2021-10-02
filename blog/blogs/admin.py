from django.contrib import admin
from django.shortcuts import render,redirect
from .models import *



class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
  



admin.site.register(Category,CategoryAdmin)
admin.site.register(SubCategory,SubCategoryAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(PopularBlogs)
admin.site.register(HomeSectionBlogs)
admin.site.register(BlogReply)
admin.site.register(BlogComment)

# admin.site.register(Subscribe)
