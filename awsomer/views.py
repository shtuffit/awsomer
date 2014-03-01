from django.shortcuts import render
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)
def home(request):
    return render(request, 'index.html')

