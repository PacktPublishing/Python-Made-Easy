"""
URL configuration for pyweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

    
"""
from django.contrib import admin  # Importing the admin module for Django administration
from django.urls import path, include  # Importing necessary modules for defining URL patterns
from blog.views import create_post, post_list  # Importing the 'create_post' and 'post_list' views from the 'blog' app


urlpatterns = [
    path('admin/', admin.site.urls),  # Maps the 'admin/' URL to the Django admin site
    path('', include('homepage.urls')),  # Includes URLs from the 'homepage' app
    path('create-post/', create_post, name='create_post'),  # Maps the 'create-post/' URL to the 'create_post' view
    path('post-list/', post_list, name='post_list'),  # Maps the 'post-list/' URL to the 'post_list' view
]

