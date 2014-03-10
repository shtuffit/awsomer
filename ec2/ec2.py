from boto.ec2 import connect_to_region
from boto.ec2.elb import connect_to_region as connect_to_elb_region

def connector(region='us-east-1'):
    conn = connect_to_region(region)
    return conn

def elb_connector(region='us-east-1'):
    conn = connect_to_elb_region(region)
    return conn

def reboot(instance_id):
    conn = connector()
    conn.reboot_instances(instance_ids=[instance_id,])

def shutdown(instance_id):
    conn = connector()
    conn.stop_instances(instance_ids=[instance_id,])

def start(instance_id):
    conn = connector()
    conn.start_instances(instance_ids=[instance_id,])

def terminate(instance_id):
    conn = connector()
    conn.terminate_instances(instance_ids=[instance_id,])
