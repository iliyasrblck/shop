from django.contrib import admin
from .models import *
# Register your models here.

class ImageInline(admin.TabularInline):
    model = Image
    extra = 0

class FeatureInline(admin.TabularInline):
    model = ProductFeature
    extra = 0

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'offer', 'new_prices','category', 'inventory')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name','new_prices', 'category')
    list_filter = ('new_prices','cerated', 'updated')
    inlines = (ImageInline, FeatureInline)