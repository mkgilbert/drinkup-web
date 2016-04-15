"""drinkup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from main.views import (home,
                        user_session,
                        index,
                        registration,
                        venue,
                        menu,
                        item)

urlpatterns = [
    url(r'^login/', user_session.user_login, name='user_login'),
    url(r'^logout/', user_session.user_logout, name='user_logout'),
    url(r'^register/', CreateView.as_view(template_name='register.html',
                                          form_class=UserCreationForm,
                                          success_url='/success/')),
    url(r'^success/', registration.success, name="success"),
    url(r'^$', index, name='index'),

    url(r'^user/home/(?P<user_id>\d+)/$', home, name='home'),

    url(r'user/add-venue/(?P<user_id>\d+)/$', venue.add, name='venue_add'),

    url(r'^user/home/(?P<user_id>\d+)/menu/(?P<menu_id>\d+)/$', menu, name='home'),

    url(r'user/home/(?P<user_id>\d+)/menu/(?P<menu_id>\d+)/add-item$', item.add, name='item_add'),
    url(r'user/home/(?P<user_id>\d+)/menu/(?P<menu_id>\d+)/edit-item/(?P<item_id>\d+)$', item.edit, name='item_edit'),

    url(r'^admin/', admin.site.urls),
]
