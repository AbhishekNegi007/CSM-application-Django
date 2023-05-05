"""cms_appliction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from cms_app.views import UserClass,PostClass,LikeClass

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/create/', UserClass.as_view()),
    path('users/detail/', UserClass.as_view()),
    path('users/update/', UserClass.as_view()),
    path('users/delete/', UserClass.as_view()),
    
    path('post/create/', PostClass.as_view()),
    path('post/detail/', PostClass.as_view()),
    path('post/update/', PostClass.as_view()),
    path('post/delete/', PostClass.as_view()),
    
    path('like/create/', LikeClass.as_view()),
    path('like/detail/', LikeClass.as_view()),
    path('like/update/', LikeClass.as_view()),
    path('like/delete/', LikeClass.as_view()),
]
