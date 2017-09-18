from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'atikucare.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'atiku.views.page', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^visualize/', 'atiku.view.visualize.page', name='visualize'),
    url(r'^index/', 'atiku.views.page', name='home'),
    url(r'^getdetails/', 'atiku.view.getdetails.getdetails', name='states'),
]
