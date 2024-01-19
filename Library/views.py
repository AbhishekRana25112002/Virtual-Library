from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from .models import Profile,Post,Comments,Books, Reviews
from django.contrib.auth.decorators import login_required
from twilio.rest import Client
from django.db.models import Q


# Create your views here.
@login_required(login_url='login')
def index(request):
    posts=Post.objects.all()
    books=Books.objects.order_by('-uploaded_at')     
    context={
        'username':request.user.username,
        'posts':posts,
        'books':books
    }
    return render(request, 'index.html',context)

def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        user= auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            user=User.objects.create_user(username=username, email=email,password=password)
            user.save()

            #log user in and redirect to settings page
            user_login=auth.authenticate(username=username,password=password)
            auth.login(request,user_login)
                
            #Create a profile object for new user
            user_model=User.objects.get(username=username)
            new_profile=Profile.objects.create(user=user_model,id_user=user_model.id)
            new_profile.save()
            return redirect('index')

    else:
        return render(request,'login.html')

@login_required(login_url='login')  
def addblog(request):
    if request.method=="POST":
        name=request.POST["name"]
        title=request.POST["title"]
        subtitle=request.POST["subtitle"]
        content=request.POST["content"]
        image=request.FILES.get('image')
        new_post=Post.objects.create(user=name, image=image, title=title, subtitle=subtitle, content=content)
        new_post.save()        
        return redirect('/')
    else:
        return render(request,'add-blog.html')
    
@login_required(login_url='login')
def addbook(request):
    if request.method=="POST":
        name=request.POST["name"]
        title=request.POST["title"]
        image=request.FILES.get('image')
        category=request.POST['category']
        author=request.POST['author']
        about=request.POST["about"]
        book=request.FILES.get('book')
        new_book=Books.objects.create(name=name,category=category, image=image, title=title, author=author, about=about, book=book)
        new_book.save()        
        return redirect('all-books')
    
    else:
        return render(request,'add-book.html')

@login_required(login_url='login')
def allposts(request):
    posts=Post.objects.all()
    context={
        'posts':posts
    }
    return render(request,'blog-grid.html',context)

@login_required(login_url='login')
def post(request,id):
    post=Post.objects.filter(id=id)[0]
    comments=Comments.objects.filter(post=post)
    context={
        'post': post,
        'comments':comments
    }
    if request.method=="POST":
        name=request.POST['name']
        comment=request.POST['comment']
        new_comment=Comments.objects.create(post=post,name=name,comment=comment)
        new_comment.save()  
    
    return render(request,'blog-single.html',context)

@login_required(login_url='login')
def getbook(request,title):
    book=Books.objects.filter(title=title)[0]
    reviews=Reviews.objects.filter(book=book)
    context={
        'book':book,
        'reviews':reviews
    }
    if(request.method=="POST"):
        name=request.POST['name']
        review=request.POST['review']
        new_review=Reviews.objects.create(name=name, comment=review,book=book)
        new_review.save()    
    return render(request,'get-book.html',context)

@login_required(login_url='login')
def download(request,title):
    book=Books.objects.filter(title=title)[0]
    if(request.method=="POST"):
        pdf_file = get_object_or_404(Books, title=title)
        response = HttpResponse(pdf_file.book, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{pdf_file.title}.pdf"'
        return response
    return redirect('/')


@login_required(login_url='login')
def allbooks(request):
    books=Books.objects.order_by('-uploaded_at')     
    context={
        'books':books
    }
    return render(request,'all-books.html',context)


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')

def contact(request):
    account_sid='AC7f538cde22899d3e4520523ed21164aa'
    auth_token="443e389f144466d402445f2cdef7c2d6"
    if request.method=="POST":
        name = request.POST['name']
        email= request.POST['email']
        message= request.POST['message']
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=f"{name}\n{email}\n{message}\n",
            from_='+12345401800',
            to='+917037632200'
        )
        print(message.sid)
        return redirect('thanks')
    
def thanks(request):
    context={
        'username':request.user.username
    }
    return render(request,'thanks.html')


def search(request):
    if request.method=="POST":
        query=request.POST['search']
        return redirect(f'/search-results/{query}')
    return render(request,'search-bar.html')

def search_results(request,title):
    books = Books.objects.filter(
        Q(title__icontains=title) | 
        Q(author__icontains=title) |
        Q(name__icontains=title) |
        Q(category__icontains=title) |
        Q(about__icontains=title) 
    )
    
    context={
        'books':books,
        'query':title
    }
    return render(request,'search-results.html',context)
