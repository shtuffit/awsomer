from django.shortcuts import render
import boto.route53
from .route53 import connector
from .forms import AddHostedZoneForm

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
    records = conn.get_all_rrsets(zone_id)

    return render(request, 'route53/zone.html', {
            'zone': zone,
            'records': records,
        })  

