import boto.route53
from boto.route53.record import ResourceRecordSets

def connector(region='us-east-1'):
    conn = boto.route53.connect_to_region(region)
    return conn

def zone_clone(source, dest):
    conn = connector()
    changes = ResourceRecordSets(conn, dest.id)
    for record in source.get_records():
      if record.type != 'NS' and record.type != 'SOA':
        new = record.name.replace(source.name, dest.name)
        if record.alias_dns_name:
          change = changes.add_change("CREATE", new, record.type, record.ttl, alias_dns_name=record.alias_dns_name, alias_hosted_zone_id=record.alias_hosted_zone_id, alias_evaluate_target_health=False)
        else:
          change = changes.add_change("CREATE", new, record.type, record.ttl)
          change.add_value(record.to_print())
    changes.commit()
