from django import forms

class AddHostedZoneForm(forms.Form):
    name = forms.CharField()
    comment = forms.CharField(required=False)

class AddRecordForm(forms.Form):
    TYPES = (
        ('A', 'A'),
        ('AAAA', 'AAAA'),
        ('CNAME', 'CNAME'),
        ('MX', 'MX'),
        ('NS', 'NS'),
        ('PTR', 'PTR'),
        ('SOA', 'SOA'),
        ('SPF', 'SPF'),
        ('SRV', 'SRV'),
        ('TXT', 'TXT'),
    )
    name = forms.CharField()
    recordtype = forms.ChoiceField(choices=TYPES)
    value = forms.CharField()
    ttl = forms.IntegerField(label='TTL')

class CloneZoneForm(forms.Form):
    name = forms.CharField(label="New Zone Domain")
    comment = forms.CharField(required=False)


