from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'sqs.views.queues', name='sqs_home'),
    url(r'^queues/$', 'sqs.views.queues'),
    url(r'^queues/(?P<queue_name>[-\w]+)', 'sqs.views.queue'),
)
