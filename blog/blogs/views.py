from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail
from .tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.defaultfilters import slugify



def base(request):
    home        =  HomeSectionBlogs.objects.all()
    bags        =  Blog.objects.filter(category__slug = "bags")
    wallets     =  Blog.objects.filter(category__slug = "wallet")
    shoes       =  Blog.objects.filter(category__slug = "shoes")

    context = {
        "home":home,
        "bags":bags,
        "wallets":wallets,
        "shoes": shoes,
    }
    return render(request, 'home.html',context)


def BlogList(request, category_slug = None):
    #-------------- Variables Declaration ------
    categories       = None
    subcategories    = None
    subcategory_blog = None
    popular_section  = None
    #-------------- Categories -----------------
    blog             = Blog.objects.all()
    if category_slug:
        try:
            categories    =   Category.objects.get(slug = category_slug)
            subcategories =   SubCategory.objects.filter(category__slug = categories.slug)
            blog          =   Blog.objects.filter(category=categories)
    #-------------- Sub Categories -------------
        except:
            subcategory_blog   =   SubCategory.objects.get(slug     = category_slug)
            blog               =   Blog.objects.filter(sub_category = subcategory_blog)

    #-------------- Popular Blogs --------------
    popular_section = PopularBlogs.objects.all()[0:3]
    print(popular_section)

    #-------------- Pagination -----------------
    paginator = Paginator(blog ,10) # Shows only 10 records per page
    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer, deliver first page.
        blogs = paginator.page(1)
    except EmptyPage:
    # If page is out of range (e.g. 7777), deliver last page of results.
        blogs = paginator.page(paginator.num_pages)
        
    for i in (blogs):
        i.description=i.description[:50]
    context = {
        'blogs':blogs,
        "categories":categories,
        "subcategories":subcategories,
        "subcategory_blog":subcategory_blog,
        "popular_section":popular_section,

    }
    return render(request,'bloglist.html',context)

def BlogDetail(request,slug):
    blogs_list   = Blog.objects.all()
    blogs = Blog.objects.get(slug=slug)
    comments= BlogComment.objects.filter(blog=blogs)
    replies = BlogReply.objects.all()
    form = Comment()
    form_1 = Reply()
    if request.method =='POST':
         form=Comment(request.POST or None)
         if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.blog=blogs
            new_comment.save()
            form.save()
            return HttpResponseRedirect(reverse('detail', args=[slug]))
             
 
    context = {
        'blogs':blogs,
        'comments':comments,
        'list':blogs_list,
        'form':form,
        'replies' : replies,
        'form_1' : form_1,
    }
    return render(request,'blogdetail.html',context)

def search(request):
    blogs_list   = Blog.objects.all()

    query=request.GET.get('search',None)
    print(query)
    blogs=Blog.objects.all()
    if query is not None:
        blogs=blogs.filter(
        Q(title__icontains=query)|
        Q(description__icontains=query)|
        Q(author__username__icontains=query)

        )
    print(blogs)
    context={
        "list": blogs_list,
        'blogs':blogs,
        "query":query
}

    return render(request,'search.html',context)

def ReplyPage(request,id, slug):
    comment=BlogComment.objects.get(id=id)
    form = Reply()
    if request.method=='POST':
        form = Reply(request.POST or None)
        if form.is_valid:
            new = form.save(commit=False)
            new.comment=comment
            new.save()
            form.save()
            return HttpResponseRedirect(reverse('detail', args = [slug]))
                
    context={
    'form1':form,
    'comment': comment,
    'slug' : slug,
    }
    return render(request,'blogReply.html',context)



def blogFormView(request):
    form = blogform()
    if request.method=='POST':
        form = blogform(request.POST ,  request.FILES)
        if form.is_valid():
            new = form.save(commit=False)
            new.author=request.user
            new.slug=slugify(new.title)
            new.save()
            form.save()
            return redirect('list')
                
    context={
    'form':form,

    }
    return render(request,'blogform.html',context)




# def BlogAuthors(request):
#     authors = BlogAuthor.objects.all()
#     context = {
#         'authors':authors
#     }

#     return render(request,'authorlist.html',context)

# def BlogListByAuthor(request,id):
#     target_author  = BlogAuthor.objects.get(id=id)
#     print(target_author)
#     blogs          = Blog.objects.filter(author=target_author)
#     context = {
#         'blogs':blogs,
#         'author':target_author
#     }
#     return render(request,'authorblogs.html',context)


# def sub(request):
#     form = subscribe()
#     if request.method == 'POST':
#         form = subscribe(request.POST or None)
#         if form.is_valid():
#             form.save()
#     context = {
#        'form':form,
#    }
    
#     return render(request,'subscribe.html',context)

# def Contact(request):
#     form = contact()
#     subject = 'contact blog'
#     if request.method=='POST':
#         form = contact(request.POST or None)
#         if form.is_valid():
#             name=form.cleaned_data.get('Name')
#             email=form.cleaned_data.get('Email')
#             message = form.cleaned_data.get('Message')
#             email_from=email
#             send_mail( subject, message, email_from, recipient_list=[settings.EMAIL_HOST_USER,email_from] )
#             return redirect('list')
#     return render(request,'contact.html',{'form':form})




# def sub(request):
#     if request.method!='POST':
#         form = subscribe()
    
#     else:
#         form = subscribe(request.POST)
#         if form.is_valid():
#            form.save()
#            current_site = get_current_site(request)
#            message = render_to_string('acc_active_email.html', {
#                 'form':form, 'domain':current_site.domain,
#                 'uid': urlsafe_base64_encode(force_bytes(form)),
#                 'token': account_activation_token.make_token(form),
#             })
#            mail_subject = 'Activate your blog account.'
#            to_email = form.cleaned_data.get('email').lower()
#            email = EmailMessage(mail_subject, message, to=[to_email])
#            email.send()
            
#            return render(request, 'acc_active_email_confirm.html')
#     return render(request, 'subscribe.html', {'form' : form, })

# def activate(request, uidb64, token):
#     uid = force_text(urlsafe_base64_decode(uidb64))
      
#         #login(request, user)
#         #return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
#     return redirect('list')
 



