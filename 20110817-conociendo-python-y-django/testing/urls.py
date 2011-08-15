from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testing.views.home', name='home'),
    # url(r'^testing/', include('testing.foo.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^books/$', 'book.views.list'),
    url(r'^book/(?P<book_slug>[-\w]+)/$', 'book.views.get', name="get-book"),
)
