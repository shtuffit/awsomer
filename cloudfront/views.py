from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page
from .forms import *
from .cloudfront import connector
import boto.cloudfront

def distributions(request):
    conn = connector()
    if request.POST:
        form = AddDistributionForm(request.POST)
        if form.is_valid():
            conn.create_distribution(form.cleaned_data['name'])
            return redirect('/cloudfront/distributions/' + form.cleaned_data['name'])
    dists = conn.get_all_distributions()

    form = AddDistributionForm()
    return render(request, 'cloudfront/distributions.html', {
            'form': form,
            'distributions': dists
        })  

def distribution(request, distribution_name):
    conn = connector()
    distribution = conn.get_all_distributions(prefix=distribution_name)[0]
    if request.POST:
        if '_clear' in request.POST:
            distribution.clear()
            return redirect('/cloudfront/distributions/' + distribution_name)
        # will have to wait for s3 integration
        #if '_dump' in request.POST:
        #    distribution.save_to_s3('cloudfront_dump')
        elif '_delete' in request.POST:
            distribution.delete()
            return redirect('/cloudfront/distributions/')
        form = AddMessageForm(request.POST)
        if form.is_valid():
            m = RawMessage()
            m.set_body(form.cleaned_data['message']) 
            count = form.cleaned_data['count']
            while count: 
                distribution.write(m)
                count -= 1
            return redirect('/cloudfront/distributions/' + distribution_name)
    else:
        form = AddMessageForm()

    item = distribution.get_attributes()
    item['name'] = distribution.name

    return render(request, 'cloudfront/distribution.html', {
            'distribution': item,
            'form': form,
        })  

