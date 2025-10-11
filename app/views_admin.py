from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from functools import wraps
from django.contrib import messages
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Page, Article
from .forms_admin import formPageEdit, formPageCreate, formArticleCreate, formArticleEdit
from uuid import UUID
from .decorators_admin import admin_required, check_useradmin


@check_useradmin
@admin_required
def page_list(request):
    pages = Page.objects.all()
    context = {
        'pages': pages,
        'title': 'Page List',
        'heading': 'Page List',
    }
    return render(request, 'admin_managed/page_list.html', context)

@check_useradmin
@admin_required
def article_list(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
        'title': 'Artikel List',
        'heading': 'Artikel List',
    }
    return render(request, 'admin_managed/article_list.html', context)


@check_useradmin
@admin_required
def article_create(request):
    if request.method == 'POST':
        form = formArticleCreate(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            if 'status' in form.cleaned_data:
                article.status = form.cleaned_data['status']
            
            article.save()
            messages.success(request, 'Artikel berhasil dibuat!')
            return redirect('app:article_list')
        else:
            messages.error(request, 'Terjadi kesalahan. Silakan periksa form Anda.')
            print("Form errors:", form.errors)
    else:
        form = formArticleCreate()
    
    context = {
        'form': form,
        'title': 'Buat Artikel Baru',
        'heading': 'Buat Artikel Baru',
    }
    return render(request, 'admin_managed/article_create.html', context)

@check_useradmin
@admin_required
def article_delete(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        article.delete()
        messages.success(request, 'Artikel berhasil dihapus!')
        return redirect('app:article_list')
    else:
        # If accessed via GET, redirect to list with error message
        messages.error(request, 'Metode tidak diizinkan untuk menghapus artikel.')
        return redirect('app:article_list')

@check_useradmin
@admin_required
def page_create(request):
    if request.method == 'POST':
        form = formPageCreate(request.POST)
        if form.is_valid():
            page = form.save(commit=False)
            page.author = request.user
            page.save()
            messages.success(request, 'Page berhasil dibuat!')
            return redirect('app:page_list')
        else:
            messages.error(request, 'Terjadi kesalahan. Silakan periksa form Anda.')
            print("Form errors:", form.errors)
    else:
        form = formPageCreate()
    
    context = {
        'form': form,
        'title': 'Buat Page Baru',
        'heading': 'Buat Page Baru',
    }
    return render(request, 'admin_managed/page_create.html', context)

@check_useradmin
@admin_required
def article_edit(request, id):
    article = get_object_or_404(Article, id=id)
    
    if request.method == 'POST':
        form = formArticleEdit(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Artikel berhasil diperbarui!')
            return redirect('app:article_list')
        else:
            messages.error(request, 'Terjadi kesalahan. Silakan periksa form Anda.')
            print("Form errors:", form.errors)
    else:
        form = formArticleEdit(instance=article)
    
    context = {
        'article': article,
        'form': form,
        'title': 'Edit Artikel',
        'heading': 'Edit Artikel',
    }
    return render(request, 'admin_managed/article_edit.html', context)


@check_useradmin
@admin_required
def page_edit(request, id):
    page = get_object_or_404(Page, id=id)
    
    if request.method == 'POST':
        form = formPageEdit(request.POST, instance=page)
        if form.is_valid():
            form.save()
            messages.success(request, 'Page berhasil diperbarui!')
            return redirect('app:page_list')
        else:
            messages.error(request, 'Terjadi kesalahan. Silakan periksa form Anda.')
            print("Form errors:", form.errors)
    else:
        form = formPageEdit(instance=page)
    
    context = {
        'page': page,
        'form': form,
        'title': 'Edit Page',
        'heading': 'Edit Page',
    }
    return render(request, 'admin_managed/page_edit.html', context)

@check_useradmin
@admin_required
def page_delete(request, id):
    page = get_object_or_404(Page, id=id)
    if request.method == 'POST':
        page.delete()
        messages.success(request, 'Page berhasil dihapus!')
        return redirect('app:page_list')
    else:
        # If accessed via GET, redirect to list with error message
        messages.error(request, 'Metode tidak diizinkan untuk menghapus page.')
        return redirect('app:page_list')
