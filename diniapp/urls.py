from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'dini.views.load_home_page', name='home'),
    url(r'^login/', 'dini.views.login'),
    url(r'^check_login/', 'dini.views.check_login' ),
    url(r'^registration_form/', 'dini.views.registration_form'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/', 'dini.views.registration'),
    url(r'show_users/', 'dini.views.show_users'),
)
