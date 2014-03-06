from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page
import boto.ec2
from .ec2 import connector, reboot, shutdown, start, terminate

@cache_page(5)
def instances(request):
    conn = connector()
    instances = []
    reservations = conn.get_all_instances()
    for res in reservations:
        item = {}
        instance = res.instances[0]
        item['name'] = instance.tags['Name']
        item['env'] = instance.tags['Environment']
        item['state'] = instance.state
        item['id'] = instance.id
        instances.append(item)

    return render(request, 'ec2/instances.html', {
            'instances': instances
        })  

@cache_page(5)
def instance(request, instance_id):
    if request.POST:
        if '_reboot' in request.POST:
            reboot(instance_id)
        elif '_shutdown' in request.POST:
            shutdown(instance_id)
        elif '_start' in request.POST:
            start(instance_id)
        elif '_terminate' in request.POST:
            terminate(instance_id)
        return redirect('/ec2/instances/' + instance_id)

    conn = connector()
    reservation = conn.get_all_instances(instance_ids=[instance_id])[0]
    instance = reservation.instances[0]

    return render(request, 'ec2/instance.html', {
            'instance': instance
        })  

