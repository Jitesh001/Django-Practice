"""
URL configuration for django090524 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from djangomidleware import views as middleware_views
from djangoauth import views as djangoauth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('django0123/', include('django0123.urls')),
    path('djangoform/', include('djangoform.urls')),
    path('middleware/', middleware_views.middlewareTest1, name='midtest1'),
    path('exception/', middleware_views.middlewareTest2, name='midtest2'),
    path('template/', middleware_views.middlewareTest3, name='midtest3'),
    path('auth/', include('djangoauth.urls')),
]
