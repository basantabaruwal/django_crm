from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages

HOME_URL = 'home'
DASHBOARD_URL = 'dashboard'

def not_for_authenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, "You're already logged in as {}".format(request.user.username))
            if 'HTTP_REFERER' in request.META:
                return redirect(request.META['HTTP_REFERER']) 
            else:
                return redirect(DASHBOARD_URL)
        else:
            return view_func(request, *args, **kwargs)
    
    return wrapper_func