from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Temporary view for the root URL
def home(request):
    return HttpResponse("Welcome to the Stock Management System!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Includes the URLs for your `api` app
    path('', home),  # Route for the root URL
]
