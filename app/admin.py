from django.contrib import admin
from django.db import models
from .models import UserAdmin, Article, Category, Page, Testimoni, Product, ProductType


admin.site.register(UserAdmin)
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Page)
admin.site.register(Testimoni)
admin.site.register(ProductType)
admin.site.register(Product)
