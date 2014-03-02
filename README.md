#AWSomer
AWSomer (pronounced awesomer) is a AWS dashboard built on Django 1.6. The only requirements should be django, boto and having boto configured corectly. AWSomer is still under heavy development, please let me know any [issues](https://github.com/shtuffit/awsomer/issues) you have.

##Services
*EC2
*SQS

##Setup
1. Clone the AWSomer repo
```
git clone https://github.com/shtuffit/awsomer.git
```

2. Install dependencies
```
pip install Django boto
```

3. Sync the database 
```
python manage.py syncdb
```

4. Run the project
```
python manage.py runserver
```

5. Start AWSomering, go to [http://localhost:8000](http://localhost:8000) in your browser
