from django.contrib import admin
from django.urls import path, include
from core.views import ProductAPIView, ProductDetail, CategoryAPIView, CategoryDetail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/products/', ProductAPIView.as_view(), name="products"),
    path('api/products/<int:id>/', ProductDetail.as_view(), name="productId"),
    path('api/categories/', CategoryAPIView.as_view(), name="categories"),
    path('api/categories/<int:id>/', CategoryDetail.as_view(), name="categoryId"),
]
