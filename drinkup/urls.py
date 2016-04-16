from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from main.views import (home, user_session, index, registration, venue, menu, item, employee,)


urlpatterns = [
    url(r'^login/', user_session.user_login, name='user_login'),
    url(r'^logout/', user_session.user_logout, name='user_logout'),
    url(r'^register/', CreateView.as_view(template_name='register.html',
                                          form_class=UserCreationForm,
                                          success_url='/success/')),
    url(r'^success/', registration.success, name="success"),
    url(r'^$', index, name='index'),

    url(r'^user/home/(?P<user_id>\d+)/$', home, name='home'),

    url(r'^user/home/(?P<user_id>\d+)/edit-user/$', user_session.user_edit, name='user_edit'),

    url(r'user/add-venue/(?P<user_id>\d+)/$', venue.add, name='venue_add'),

    url(r'^user/home/(?P<user_id>\d+)/(?P<venue_id>\d+)/add-employee/$', employee.add, name='employee_add'),

    url(r'^user/home/(?P<user_id>\d+)/(?P<venue_id>\d+)/employee/(?P<employee_id>\d+)/edit-employee/$', employee.edit, name='employee_edit'),

    url(r'user/home/(?P<user_id>\d+)/(?P<venue_id>\d+)/edit-venue/$', venue.edit, name='venue_edit'),

    url(r'^user/home/(?P<user_id>\d+)/(?P<venue_id>\d+)/add-menu/$', menu.add, name='menu_add'),

    url(r'^user/home/(?P<user_id>\d+)/menu/(?P<menu_id>\d+)/edit-menu/$', menu.edit, name='menu_edit'),

    url(r'^user/home/(?P<user_id>\d+)/menu/(?P<menu_id>\d+)/$', menu.display, name='menu'),

    url(r'user/home/(?P<user_id>\d+)/menu/(?P<menu_id>\d+)/add-item$', item.add, name='item_add'),

    url(r'user/home/(?P<user_id>\d+)/menu/(?P<menu_id>\d+)/edit-item/(?P<item_id>\d+)$', item.edit, name='item_edit'),

    url(r'^admin/', admin.site.urls),

    url(r'^', include('main.urls')),

]
