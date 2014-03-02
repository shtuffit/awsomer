from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page
import boto.sqs

def connector(region='us-east-1'):
    conn = boto.sqs.connect_to_region(region)
    return conn

def queues(request):
    conn = connector()
    queues = []
    ques = conn.get_all_queues()
    for que in ques:
        item = {}
        item['name'] = que.name 
        item['attrib'] = que.get_attributes()
        queues.append(item)

    return render(request, 'sqs/queues.html', {
            'queues': queues
        })  

def queue(request, queue_name):
    print queue_name
    conn = connector()
    queue = conn.get_all_queues(prefix=queue_name)[0]

    item = queue.get_attributes()
    item['name'] = queue.name

    return render(request, 'sqs/queue.html', {
            'queue': item,
        })  

