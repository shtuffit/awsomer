from django.shortcuts import render, redirect
import boto.route53
from .route53 import connector, zone_clone
from .forms import AddHostedZoneForm, CloneZoneForm

def zones(request):
    conn = connector()
    if request.POST:
        form = AddHostedZoneForm(request.POST)
        if form.is_valid():
            conn.create_hosted_zone(form.cleaned_data['name']) 
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
        form = CloneZoneForm(request.POST)
        if form.is_valid():
            zoneB = conn.create_zone(form.cleaned_data['name'], comment=form.cleaned_data['comment']) 
            zone_clone(obj, zoneB)
            return redirect('/route53/zones/' + zoneB.id)


    records = conn.get_all_rrsets(zone_id)
    form = CloneZoneForm()

    return render(request, 'route53/zone.html', {
            'zone': zone,
            'records': records,
            'form': form,
        })  

