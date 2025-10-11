"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include(('app.urls', 'app'), namespace='app'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf.urls import handler404
from .views import custom_404


urlpatterns = [
    # URL yang tidak perlu prefix bahasa
    path('admin_managed/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    
]

# URL yang akan mendapat prefix bahasa (/en/, /id/)
urlpatterns += (
    path('dashboard/', include(('app.urls', 'app'), namespace='app')),
    path('login/', views.loginView, name='login'),
    path('about', views.about, name='about'),
    path('', views.index, name='index'),
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),
    path('article/', views.article_list, name='article_list'),
    path('category/<slug:slug>/', views.category_articles, name='category_articles'),
    path('page/<slug:slug>/', views.page_detail, name='page_detail'),

)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'core.views.custom_404'