"""bookmark_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from app.views import BookmarkView, BookmarkCreateView, redirect_view, UserCreateView, \
                      BookmarkUpdateView, BookmarkDeleteView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', BookmarkView.as_view(), name="bookmark_view"),
    url(r'^bookmarks/create_user/$', UserCreateView.as_view(), name="user_create_view"),
    url (r'^bookmarks/create/$', BookmarkCreateView.as_view(), name="bookmark_create_view"),
    url (r'^bookmarks/update/(?P<pk>\d+)/$', BookmarkUpdateView.as_view(), name="bookmark_update_view"),
    url (r'^bookmarks/delete/(?P<pk>\d+)/$', BookmarkDeleteView.as_view(), name="bookmark_delete_view"),
    url (r'^bookmarks/(?P<short_url>\w+)/$', redirect_view, name="redirect_view"),

]
