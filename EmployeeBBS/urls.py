"""EmployeeBBS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth import views as AuthViews
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from users import views as userView

urlpatterns = [
    path('', userView.homeAuthCheck),
    path('admin/', admin.site.urls),
    path('home/', AuthViews.LoginView.as_view(template_name = 'users/homepage.html'), name = 'home'),
    path('login/', userView.Login, name = 'login'), 
    path('logout/', userView.Logout, name = 'logout'),
    path('register/', userView.Register, name = 'register'),
    path('bbs/', include('bbs.urls')),
    path('events/', include('events.urls')),
    path('posts/', include('posts.urls')),
    path('users/', include('users.urls')),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)