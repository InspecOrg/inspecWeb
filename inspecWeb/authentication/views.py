"""Views for authentication app."""

from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.views.generic import View
from django.contrib.auth import authenticate, login


class Login(View):
    """Login methods for auth."""

    http_method_names = [u'get', u'post']

    def get(self, request):
        """Get method for login."""
        if request.user.is_authenticated():
            response = render_to_response(
                'home.html', context_instance=RequestContext(request))
        else:
            response = render_to_response(
                'login.html', context_instance=RequestContext(request))
        return response

    def post(self, request):
        """POST method for login."""
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            response = render_to_response(
                'home.html', context_instance=RequestContext(request))
        else:
            response = redirect('/login/')
        return response
