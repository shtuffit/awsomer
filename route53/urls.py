from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'route53.views.zones', name='route53_home'),
    url(r'^zone/$', 'route53.views.zones'),
    url(r'^zone/(?P<zone_id>[\w]+)', 'route53.views.zone'),
)
