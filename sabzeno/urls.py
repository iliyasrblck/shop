from django.urls import path

from . import views

app_name = 'sabzeno'

urlpatterns = [
    # لست تمام محصولات
    path('products/', views.product_list, name='PR-list'),

    # تمام محصولات یک کتگوری
    path('products/<slug:category_slug>/', views.product_list, name='PR-CG-list'),

    #مشخصات یک محصول
    path('product/<int:product_id>/<slug:slug>', views.product_detail, name='PR-detail'),


]