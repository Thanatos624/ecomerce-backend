from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def root_view(request):
    return JsonResponse({"message": "Welcome to the eCommerce API"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),  # User app endpoints
    path('api/products/', include('products.urls')),  # Product app endpoints (if created)
    path('api/orders/', include('orders.urls')),  # Orders app endpoints (if created)
    path('', root_view),  # Root route
]
