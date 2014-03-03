from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page
from .forms import *
import boto.sqs
from boto.sqs.message import Message

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
        try:
            item['attrib'] = que.get_attributes()
        except SQSError:
            pass
        queues.append(item)

    return render(request, 'sqs/queues.html', {
            'queues': queues
        })  

def queue(request, queue_name):
    conn = connector()
    queue = conn.get_all_queues(prefix=queue_name)[0]
    if request.POST:
        form = AddMessageForm(request.POST)
        if form.is_valid():
            m = Message()
            m.set_body(form.cleaned_data['message']) 
            count = form.cleaned_data['count']
            while count: 
                queue.write(m)
                count -= 1
            return redirect('/sqs/queue/' + queue_name)
    else:
        form = AddMessageForm()

    item = queue.get_attributes()
    item['name'] = queue.name

    return render(request, 'sqs/queue.html', {
            'queue': item,
            'form': form,
        })  

