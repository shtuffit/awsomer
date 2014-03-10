from django.shortcuts import render, redirect
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

def distribution(request, distribution_id):
    conn = connector()
    distribution_config = conn.get_distribution_config(distribution_id)
    distribution_info = conn.get_distribution_info(distribution_id)

    return render(request, 'cloudfront/distribution.html', {
            'config': distribution_config,
            'info': distribution_info,
        })  

