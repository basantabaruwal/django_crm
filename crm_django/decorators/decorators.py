from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages

HOME_URL = 'home'
DASHBOARD_URL = 'dashboard'


def not_for_authenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, "You're already logged in as {}".format(
                request.user.username))
            if 'HTTP_REFERER' in request.META:
                return redirect(request.META['HTTP_REFERER'])
            else:
                return redirect(DASHBOARD_URL)
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_groups(allowed_groups=[]):
    if not allowed_groups:  # just bypass some unwanted bugs # remember toptal python hiring post
        allowed_groups = []
    print("******************* Allowed groups: ", allowed_groups)
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group_names = []
            if request.user.groups.exists():
                # extract group names from user assigned groups
                group_names = [group.name for group in request.user.groups.all()]
                print("******************* Group Names: ", group_names)
            
            # extract group names that are common in both lists
            group_names_common = [name for name in group_names if name in allowed_groups]
            print("******************* Common Group Names: ", group_names)
            if group_names_common:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You are not authorized!!")
        return wrapper_func
    return decorator




def staff_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    '''
    Decorator for views that checks that the logged in user is a staff,
    redirects to the log-in page if necessary.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_staff,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

