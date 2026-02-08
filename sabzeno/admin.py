from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# --------------------------------------------------

class ImageInline(admin.TabularInline):
    model = Image
    extra = 0


class FeatureInline(admin.TabularInline):
    model = ProductFeature
    extra = 0

class AddressInline(admin.TabularInline):
    model = Address
    extra = 0

# -------------------------------------------------------------
# Register your models here.

@admin.register(Users)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name','last_name', 'phone')
    fieldsets = UserAdmin.fieldsets + (
    ('اطلاعات بیشتر', {'fields': ('phone','birthday')}),
    )
    search_fields = ('username', 'first_name', 'last_name', 'phone')
    list_filter = ('first_name', 'last_name', 'phone', 'email', 'birthday')
    inlines = (AddressInline,)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'offer', 'new_prices', 'category', 'inventory')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'new_prices', 'category')
    list_filter = ('new_prices', 'cerated', 'updated')
    inlines = (ImageInline, FeatureInline)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'Province', 'city']
    list_filter = ['Province', 'city']
    search_fields = ['Province', 'city' , 'user__username', 'user__first_name', 'user__last_name', 'full_address']