import boto.rds2

def connector(region='us-east-1'):
    conn = boto.rds2.connect_to_region(region)
    return conn

def get_instances(conn=connector(), instances=None):
    return conn.describe_db_instances(db_instance_identifier=instances)['DescribeDBInstancesResponse']['DescribeDBInstancesResult']['DBInstances']
