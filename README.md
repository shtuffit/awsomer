#AWSomer
AWSomer (pronounced awesomer) is a AWS dashboard built on Django 1.6. The only requirements should be django, boto and having boto configured with a IAM user with access to the supported services. AWSomer is still under heavy development, please let me know any issues you have or you would like to see added [here](https://github.com/shtuffit/awsomer/issues) 

##Services
* EC2
* Route53
* SQS

##Setup
1. Clone the AWSomer repo
```
git clone https://github.com/shtuffit/awsomer.git
```

2. Install dependencies
```
pip install Django boto
```

3. Comment out unused services in awsomer/setttings.py INSTALLED_APPS to keep them from appearing in Navs
```
...
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'awsomer',
    'ec2',
    'route53',
#    'sqs',
)
...
```

4. Sync the database 
```
python manage.py syncdb
```

5. Run the project
```
python manage.py runserver
```

6. Start AWSomering, go to [http://localhost:8000](http://localhost:8000) in your browser


