from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django .utils import timezone
from django.core.paginator import Paginator
# Create your views here.
def home(request):
    blogs= Blog.objects
    blog_list = Blog.objects.all()

    paginator= Paginator(blog_list,3)

    page = request.GET.get('page')
    
    posts = paginator.get_page(page)
    return render(request,'home.html',{'blogs':blogs, 'post':posts} ) 

def detail(request, blog_id):
    details= get_object_or_404(Blog,pk=blog_id)

    return render(request,'detail.html',{'details':details} )      

def new(request):
    return render(request,'new.html')

def create(request):
    blog=Blog()
    blog.title=request.GET['title']
    blog.body=request.GET['body']
    blog.pub_date=timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))