from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'route53.views.zones', name='route53_home'),
    url(r'^zones/$', 'route53.views.zones'),
    url(r'^zones/(?P<zone_id>[\w]+)', 'route53.views.zone'),
    url(r'^zones/(?P<zone_id>[\w]+)/clone', 'route53.views.clone_zone'),
)
