from django.contrib import admin
from django.urls import path, include
from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('products/', views.productsList, name='products-list'),
    path('products/<int:id>', views.productView, name='product-views'),
    path('products/create/', views.productCreate, name='product-create'),
    path('products/edit/<int:id>', views.productEdit, name='product-edit'),
    path('products/delete/<int:id>', views.productDelete, name='product-delete'),
    path('categories/', views.categoriesList, name='categories-list'),
    path('categories/<int:id>', views.categoryView, name='category-views'),
    path('categories/create/', views.categoryCreate, name='category-create'),
    path('categories/edit/<int:id>', views.categoryEdit, name='category-edit'),
    path('categories/delete/<int:id>', views.categoryDelete, name='category-delete'),
    path('transactions/', views.transactionsList, name='transactions-list'),
    path('products/<int:id>/transaction', views.transactionCreate, name='transaction-create'),
    path('transactions/products/<int:id>', views.transactionUpdate, name='transaction-update'),
    path('contato/', views.faleConosco, name='fale-conosco'),
]
