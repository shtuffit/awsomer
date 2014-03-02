from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'sqs.views.queues', name='sqs_home'),
    url(r'^queue/$', 'sqs.views.queues'),
    url(r'^queue/(?P<queue_name>[-\w]+)', 'sqs.views.queue'),
)
