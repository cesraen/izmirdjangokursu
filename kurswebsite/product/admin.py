from django.contrib import admin
from product.models import Category, Product
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']
    #fields = ['status]

admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    #fields = ['title, 'status']
    list_display = ['title', 'status']
    list_filter = ['status', 'category']
admin.site.register(Product, ProductAdmin)