from django.shortcuts import render, redirect
from .rds import *

def instances(request):
    instances = get_instances()
    return render(request, 'rds/instances.html', {
            'instances': instances
        })  

def instance(request, instance_name):
    instance = get_instances(instances=instance_name)[0]

    return render(request, 'rds/instance.html', {
            'instance': instance,
        })  

