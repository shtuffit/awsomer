from boto import connect_cloudfront

def connector():
    conn = connect_cloudfront()
    return conn

