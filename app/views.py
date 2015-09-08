import requests
import json

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.conf import settings
from app.forms import HealthFinderForm

YOUR_INFO = {
    'name' : 'Karthik Ravindra',
    'bio' : 'I build django based web applications',
    'email' : 'karthik.ravindra@gmail.com',
    'twitter_username' : '', # No @ symbol, just the handle.
    'github_username' : "karthikbgl", 
    'headshot_url' : '',
}

HEALTHFINDER_URL = "http://healthfinder.gov/developer/MyHFSearch.json?api_key=%s" % settings.HEALTHFINDER_API_KEY
    
def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/base.html',
        context_instance = RequestContext(request,
            {
                'attendee' : YOUR_INFO,    
                'year': datetime.now().year,
            })
    )


def health_finder(request):

    form = HealthFinderForm()

    if request.method == "POST":
        form = HealthFinderForm(request.POST)
        if form.is_valid():
            payload = form.cleaned_data
            response = requests.get(HEALTHFINDER_URL, params=payload)

            results = {}
            if response and response.text:
                response_dict = json.loads(response.text)
                results = response_dict.get('Result')

                return render(request, "app/healthfinder.html", {
                    'topics': results.get('Topics'),
                    'error': results.get('Error'),
                    'total': results.get('Total')
                })


    return render(request, "app/healthfinder.html", {'form': form})
