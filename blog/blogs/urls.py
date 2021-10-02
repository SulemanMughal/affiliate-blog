from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^$',views.base,name='home'),
    url(r'^bloglist$',views.BlogList,name='list'),
    url(r'^bloglist/(?P<category_slug>[-\w]+)$',views.BlogList,name='list'),
    url(r'^detail/(?P<slug>[-\w]+)$',views.BlogDetail,name='detail'),
    url(r'^search/',views.search,name='search'),
    url(r'^blog/',views.blogFormView,name='blog'),
    url(r'^reply/(?P<id>\d+)/(?P<slug>[-\w]+)/$',views.ReplyPage,name='reply'),


####################################################################################################



    # url(r'^authorlist/',views.BlogAuthors,name='authorlist'),    
    # url(r'^author/(?P<id>\d+)$', views.BlogListByAuthor, name="blog-by-author"),
    # # url(r'^category/(?P<slug>[-\w]+)/$', views.base, name='category'),
    # # url(r'^cat/', views.base1, name='cat'),
    # # url(r'^subscribe/',views.sub,name='subscribe'),
    # # url(r'^contact/',views.Contact,name='contact'),


]