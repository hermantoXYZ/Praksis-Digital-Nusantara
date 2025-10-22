from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from app.models import Article, Category, Page, Testimoni, Product, ProductType
from django.db.models import Count, Q
from django.utils.text import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


tanggal_now = datetime.now().date()

def custom_404(request, exception):
    return render(request, "home/404.html", status=404)

def index(request):

    all_articles = Article.objects.filter(status='published').order_by('-created_at')
    paginator = Paginator(all_articles, 6)
    page = request.GET.get('page')
    
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    
    featured_article = Article.objects.filter(status='published').order_by('-created_at').first()

    testimoni_list = Testimoni.objects.all()
    context = {
        'article_list': articles,
        'featured_article': featured_article,
        'paginator': paginator,
        'testimoni_list' : testimoni_list,
    }
    return render(request,'home/index.html', context) 


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    category_list_variabel = Category.objects.all()
    popular_articles = Article.objects.filter(status='published').order_by('-views_count')[:3]
    article.views_count += 1
    article.save()
    category_list_variabel = Category.objects.annotate(
        article_count=Count('articles', filter=Q(articles__status='published'))
    )
    latest_articles_variabel = Article.objects.filter(status='published').order_by('-created_at')[:3]
    return render(request, 'home/article_detail.html', {'article': article, 'views': article.views_count, 'category_list': category_list_variabel, 'latest_articles': latest_articles_variabel, 'popular_articles': popular_articles})

def article_list(request):
    all_articles = Article.objects.filter(status='published').order_by('-created_at')
    category_filter = request.GET.get('category')
    if category_filter:
        all_articles = all_articles.filter(category__slug=category_filter)
    
    # Filter berdasarkan pencarian
    search_query = request.GET.get('search')
    if search_query:
        all_articles = all_articles.filter(
            Q(title__icontains=search_query) | 
            Q(content__icontains=search_query) |
            Q(author__first_name__icontains=search_query) |
            Q(author__last_name__icontains=search_query)
        )
    per_page = request.GET.get('per_page', 12)
    
    if per_page == 'all':
        articles = all_articles
        paginator = None
    else:
        try:
            per_page = int(per_page)
            if per_page not in [6, 12, 24, 48]:
                per_page = 12
        except (ValueError, TypeError):
            per_page = 12
        
        paginator = Paginator(all_articles, per_page)
        page = request.GET.get('page')
        
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)
    categories = Category.objects.annotate(
        article_count=Count('articles', filter=Q(articles__status='published'))
    )
    
    context = {
        'articles': articles,
        'paginator': paginator,
        'categories': categories,
        'current_category': category_filter,
        'search_query': search_query,
    }
    return render(request, 'home/article_list.html', context)

def category_articles(request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles = Article.objects.filter(category=category, status='published').order_by('-created_at')
    return render(request, 'home/category_articles.html', {'category': category, 'articles': articles})

def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug)
    articles = Article.objects.filter(status='published').order_by('-created_at')[:3]
    latest_articles_variabel = Article.objects.filter(status='published').order_by('-created_at')[:3]
    category_list_variabel = Category.objects.annotate(
        article_count=Count('articles', filter=Q(articles__status='published'))
    )
    context = {
        'page': page,
        'articles': articles,
        'latest_articles': latest_articles_variabel,
        'category_list': category_list_variabel,
    }
    return render(request, 'home/page_detail.html', context)

def about(request):
    context = {
        'title' : 'About',
        'heading' : 'TENTANG APLIKASI' 
    }
    return render(request,'about.html', context) 


def loginView(request):
    context = {
        'title': 'Login',
        'heading': 'Login',
    }
    if request.method == "POST":
        print (request.POST)
        username_in = request.POST['username']
        password_in = request.POST['password']
        user = authenticate(request, username=username_in, password=password_in)        
        if user is not None:
            login(request, user)
            print(user)
            messages.success(request, 'Selamat Datang!')
            return redirect('/dashboard/')
        else:
            messages.warning(request, 'Periksa Kembali Username dan Password Anda!')
            return redirect('login')
    
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return render(request,'home/login.html', context) 

def product_type_list(request):
    product_types = ProductType.objects.all().order_by('name')
    context = {
        'product_types': product_types,
    }
    return render(request, 'home/product_type_list.html', context)

def products_by_type(request, slug):
    product_type = get_object_or_404(ProductType, slug=slug)
    products = Product.objects.filter(product_type=product_type)

    context = {
        'product_type': product_type,
        'products': products,
    }

    return render(request, 'home/products_by_type.html', context)

@login_required
def LogoutView(request):
    context = {
        'title': 'Login',
        'heading': 'Login Gaes',
    }
    if request.method == "POST":
        if request.POST['logout']=='ya':
            logout(request)
        return redirect('login')    

    return render(request,'logout.html', context)

