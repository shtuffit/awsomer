from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ec2.views.instances', name='ec2_home'),
    url(r'^instances/$', 'ec2.views.instances'),
    url(r'^instances/(?P<instance_id>[-\w]+)$', 'ec2.views.instance'),
    url(r'^load-balancers/$', 'ec2.views.load_balancers'),
    url(r'^load-balancers/(?P<lb_name>[-\w]+)$', 'ec2.views.load_balancer'),
)
