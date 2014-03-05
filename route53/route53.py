import boto.route53

def connector(region='us-east-1'):
    conn = boto.route53.connect_to_region(region)
    return conn

