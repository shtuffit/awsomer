from django.shortcuts import render, redirect
import boto.ec2
from .ec2 import * 

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

def load_balancers(request):
    conn = elb_connector()
    lbs = conn.get_all_load_balancers()

    return render(request, 'ec2/load_balancers.html', {
            'lbs': lbs
        })  

def load_balancer(request, lb_name):
    conn = elb_connector()
    lb = conn.get_all_load_balancers(load_balancer_names=[lb_name])[0]

    return render(request, 'ec2/load_balancer.html', {
            'lb': lb
        })  
