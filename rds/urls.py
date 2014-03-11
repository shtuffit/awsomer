from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'rds.views.instances', name='rds_home'),
    url(r'^instances/$', 'rds.views.instances'),
    url(r'^instances/(?P<instance_name>[-\w]+)', 'rds.views.instance'),
)
