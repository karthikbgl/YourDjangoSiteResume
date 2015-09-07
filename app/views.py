"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

YOUR_INFO = {
    'name' : 'Karthik Ravindra',
    'bio' : 'Code',
    'email' : 'karthik.ravindra@gmail.com',
    'twitter_username' : '', # No @ symbol, just the handle.
    'github_username' : "karthikbgl", 
    'headshot_url' : '',
}
    
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
