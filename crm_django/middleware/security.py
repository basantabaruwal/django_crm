from django.conf import settings
from django.http import HttpResponseRedirect
from functools import partial
# Avoid shadowing the login() and logout() views below.
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
from django.utils.http import urlquote


def public(function):
    """Decorator for public views that do not require authentication
    """
    orig_func = function
    while isinstance(orig_func, partial):  # if partial - use original function for authorization
        orig_func = orig_func.func
    orig_func.is_public_view = True

    return function

def is_public(function):
    try:                                    # cache is found
        return function.is_public_view
    except AttributeError:                  # cache is not found
        result = function.__module__.startswith('django.') and not function.__module__.startswith('django.views.generic') # Avoid modifying admin and other built-in views

        try:                                # try to recreate cache
            function.is_public_view = result
        except AttributeError:
            pass

        return result


class NonpublicMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception): 
        return HttpResponse("in exception")
        

    def process_view_check_logged(self, request, view_func, view_args, view_kwargs):
        return

    def process_view(self, request, view_func, view_args, view_kwargs):
        while isinstance(view_func, partial):  # if partial - use original function for authorization
            view_func = view_func.func

        request.public = is_public(view_func)
        if not is_public(view_func):
            if request.user.is_authenticated:     # only extended checks are needed
                return self.process_view_check_logged(request, view_func, view_args, view_kwargs)

            return self.redirect_to_login(request.get_full_path())  # => login page

    def redirect_to_login(self, original_target, login_url=settings.LOGIN_URL):
        return HttpResponseRedirect("%s?%s=%s" % (login_url, REDIRECT_FIELD_NAME, urlquote(original_target)))