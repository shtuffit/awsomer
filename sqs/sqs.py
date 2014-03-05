import boto.sqs

def connector(region='us-east-1'):
    conn = boto.sqs.connect_to_region(region)
    return conn

