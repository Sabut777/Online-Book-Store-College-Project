
from django.http import HttpResponse
from django.shortcuts import render,redirect

from .models import Category, Books

from django.db.models import Q

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

# from django.contrib.auth.views import LogoutView




# Create your views here.

def loginAdmin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
            # Redirect to a success page.
            else:
                redirect('login')
            ...
    # else:
    #     return HttpResponse("Sorry")
        ...
    return render (request, 'login.html')


def logoutAdmin(request):
    logout(request)
    return redirect('/')





def index(request):

    category = request.GET.get('category')
    if category == None:
        books = Books.objects.all()
    else:
        books = Books.objects.filter(category__name=category).order_by('price')
    #print(category, category)
    #print(books, books)


    categories = Category.objects.all()
    #books = Books.objects.all()
    context = {
        'categories': categories,
        'books': books,
    }
    return render(request, 'index.html', context)


def search(request):
    search_post = request.GET.get('search')
    if search_post:
        search = Books.objects.filter(Q(name__icontains=search_post) | Q(author__icontains=search_post))
    else:
        return HttpResponse('Sorry No match Found')

    categories = Category.objects.all()

    context = {
        'search': search,
        'categories': categories,
    }

    return render(request, 'search.html', context)


def orderPrice(request):
    books = Books.objects.all().order_by('-price')
    categories = Category.objects.all()

    # return render(request)

    context = {
        'categories': categories,
        'books': books,
    }
    return render(request, 'index.html', context)


def orderName(request):
    books = Books.objects.all().order_by('name')
    categories = Category.objects.all()

    # return render(request)

    context = {
        'categories': categories,
        'books': books,
    }
    return render(request, 'index.html', context)


def viewPhoto(request, pk):
    book = Books.objects.get(id=pk)
    context = {
        'book': book,
    }
    return render(request, 'viewphoto.html', context)


def addPhoto(request):
    
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])

        else:
             category = None

        book = Books.objects.create(
            category = category,
            image = image, 
            name = data['name'],
            author = data['author'],
            price = data['price'],
            description = data['description'],
        )

        return redirect('index')

        
    context = {
        'categories': categories,
    }
    return render(request, 'addphoto.html', context)

