from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'openshift.views.lawn', name='lawn'),
    url(r'^home/', 'openshift.views.lawn', name='lawn'),
    url(r'^lawn/', 'openshift.views.lawn', name='lawn'),
    url(r'^services/', 'openshift.views.services', name='lawn'),
    url(r'^about/', 'openshift.views.aboutus', name='lawn'),
    url(r'^contact/', 'openshift.views.contactus', name='lawn'),
    url(r'^lawnread/', 'openshift.views.lawnreadmore', name='lawn'),
    url(r'^satisfaction/', 'openshift.views.satisfactionreadmore', name='lawn'),
    url(r'^testimonials/', 'openshift.views.testimonialsreadmore', name='lawn'),
    url(r'^mowing/', 'openshift.views.mowing', name='lawn'),
    url(r'^shrubs/', 'openshift.views.shrubs', name='lawn'),
    url(r'^mulch/', 'openshift.views.mulch', name='lawn'),
    # url(r'^openshift/', include('openshift.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
