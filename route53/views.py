from django.shortcuts import render, redirect
import boto.route53
from .route53 import *
from .forms import *
from time import sleep

def zones(request):
    conn = connector()
    if request.POST:
        form = AddHostedZoneForm(request.POST)
        if form.is_valid():
            conn.create_hosted_zone(form.cleaned_data['name']) 
            sleep(1)
            return redirect('/route53/zones/' + zone.id)
    else:
        form = AddHostedZoneForm()

    zonelist = []
    zones = conn.get_zones()
    for zone in zones:
        item = {}
        item['name'] = zone.name 
        item['id'] = zone.id 
        item['count'] = zone.resourcerecordsetcount
        zonelist.append(item)

    return render(request, 'route53/zones.html', {
            'zones': zonelist,
            'form': form,
        })  

def zone(request, zone_id):
    conn = connector()
    zone = conn.get_hosted_zone(zone_id)['GetHostedZoneResponse']
    obj = conn.get_zone(zone['HostedZone']['Name'])

    if request.POST:
        if '_delete' in request.POST:
            obj.delete()
            return redirect('/route53/zones/')
        addrecordform = AddRecordForm(request.POST)
        if addrecordform.is_valid():
            from pprint import pprint
            pprint(addrecordform.cleaned_data)
            addrecord(obj, addrecordform.cleaned_data['name'], addrecordform.cleaned_data['recordtype'], addrecordform.cleaned_data['value'], addrecordform.cleaned_data['ttl'])
            return redirect('/route53/zones/' + zone_id)
        cloneform = CloneZoneForm(request.POST)
        if cloneform.is_valid():
            zoneB = conn.create_hosted_zone(cloneform.cleaned_data['name'], comment=cloneform.cleaned_data['comment'])['CreateHostedZoneResponse'] 
            newobj = conn.get_zone(zoneB['HostedZone']['Name'])
            zone_clone(obj, newobj)
            sleep(5)
            return redirect('/route53/zones/' + zoneB.id)


    records = conn.get_all_rrsets(zone_id)
    cloneform = CloneZoneForm()
    addrecordform = AddRecordForm()

    return render(request, 'route53/zone.html', {
            'zone': zone,
            'records': records,
            'cloneform': cloneform,
            'addrecordform': addrecordform,
        })  

