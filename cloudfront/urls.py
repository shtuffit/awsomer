from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'cloudfront.views.distributions', name='cloudfront_home'),
    url(r'^distributions/$', 'cloudfront.views.distributions'),
    url(r'^distributions/(?P<distribution_name>[-\w]+)', 'cloudfront.views.distribution'),
)
