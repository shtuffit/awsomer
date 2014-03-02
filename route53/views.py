from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page
import boto.route53

def connector(region='us-east-1'):
    conn = boto.route53.connect_to_region(region)
    return conn

def zones(request):
    conn = connector()
    zonelist = []
    zones = conn.get_zones()
    for zone in zones:
        item = {}
        item['name'] = zone.name 
        item['id'] = zone.id 
        item['count'] = zone.resourcerecordsetcount
        zonelist.append(item)

    return render(request, 'route53/zones.html', {
            'zones': zonelist
        })  

def zone(request, zone_id):
    conn = connector()
    zone = conn.get_hosted_zone(zone_id)['GetHostedZoneResponse']
    records = conn.get_all_rrsets(zone_id)

    return render(request, 'route53/zone.html', {
            'zone': zone,
            'records': records,
        })  

