from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ec2.views.instances', name='ec2_home'),
    url(r'^instance/$', 'ec2.views.instances'),
    url(r'^instance/(?P<instance_id>[-\w]+)', 'ec2.views.instance'),
)
