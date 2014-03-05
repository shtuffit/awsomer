from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page
import boto.ec2

def connector(region='us-east-1'):
    conn = boto.ec2.connect_to_region(region)
    return conn

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
    conn = connector()
    if request.POST:
        if '_reboot' in request.POST:
            conn.reboot_instances(instance_ids=[instance_id,])
        elif '_shutdown' in request.POST:
            conn.stop_instances(instance_ids=[instance_id,])
        elif '_start' in request.POST:
            conn.start_instances(instance_ids=[instance_id,])
        elif '_terminate' in request.POST:
            conn.terminate_instances(instance_ids=[instance_id,])
        return redirect('/ec2/instances/' + instance_id)

    reservation = conn.get_all_instances(instance_ids=[instance_id])[0]
    instance = reservation.instances[0]

    return render(request, 'ec2/instance.html', {
            'instance': instance
        })  

