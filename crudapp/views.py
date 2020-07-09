from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .forms import BlogUpdate



# Create your views here.

def home(request):
    blogs = Blog.objects.order_by('-id')
    blog_list = Blog.objects.all().order_by('-id')#paginator란 변수에 Pagenator를 이요해서 3개씩자른 글 목록을 넣어줌
    paginator = Paginator(blog_list,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)#페이지를 출력하기위해 posts에 넣어줌

    return render(request,'home.html', {'blogs':blogs,'posts':posts} )

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog_detail})

def create(request):
    return render(request, 'create.html')

def postcreate(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/crudapp/detail/' + str(blog.id))

def update(request, blog_id):
    blog = Blog.objects.get(id=blog_id)

    if request.method =='POST':
        form = BlogUpdate(request.POST)
        if form.is_valid():
            blog.title = form.cleaned_data['title']
            blog.body = form.cleaned_data['body']
            blog.pub_date=timezone.now()
            blog.save()
            return redirect('/crudapp/detail/' + str(blog.id))
    else:
        form = BlogUpdate(instance = blog)#기존의 해당 게시글의 정보를 가지고온다.
 
        return render(request,'update.html', {'form':form})
def delete(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    return redirect('/')

def new(request):
    full_text = request.GET['fulltext']

    word_list = full_text.split()

    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            # Increase
            word_dictionary[word] += 1
        else:
            # add to the dictionary
            word_dictionary[word] = 1

    return render(request, 'new.html', {'fulltext': full_text, 'total': len(word_list), 'dictionary': word_dictionary.items()} )

def search(request):
    blogs = Blog.objects.all().order_by('-id')#blogs에 모든 객체를 역순으로 담는다.

    q=request.POST.get('q',"")#Post로 넘어온 값을 q에 담는다.

    if q:
        blogs = blogs.filter(title__icontains=q)#blogs에 filter를 하여 icontains을 이용해서 q와 비교
        return render(request,'search.html',{'blogs' : blogs, 'q' :q})#같다면 search.html에 blogs와 q를 넘겨준다.
    else:
        return render(request,'search.html')