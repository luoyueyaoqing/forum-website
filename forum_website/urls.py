"""forum_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from website import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/', views.index_register, name='register'),
    url(r'^login/', views.index_login, name='login'),
    url(r'^logout/', views.index_logout, name='logout'),

    url(r'^$', views.index, name='index'),
    url(r'^articles/(?P<id>\d+)/', views.articles, name='articles'),
    url(r'^detail/(?P<id>\d+)/', views.detail, name='detail'),
    url(r'^add_article/(?P<id>\d+)/', views.add_article, name='add_article'),
    url(r'^comment/(?P<id>\d+)/', views.comment, name='comment'),
    url(r'^edit/(?P<id>\d+)/', views.edit, name='edit'),
    url(r'^del_article/(?P<id>\d+)/', views.del_article, name='del_article'),
    url(r'^del_comment/(?P<id>\d+)/', views.del_comment, name='del_comment'),
]
