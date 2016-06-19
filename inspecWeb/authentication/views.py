"""Views for authentication app."""

from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from authentication.models import InspecUser


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


class Logout(View):
    """Logout Method."""

    def get(self, request):
        """Get method For logout."""
        logout(request)

        return render_to_response(
            'login.html', context_instance=RequestContext(request))


class SignUp(View):
    """SingUp methods."""

    http_method_names = [u'get', u'post']

    def get(self, request):
        """Get method for SignUp, will return the page for signup."""
        return render_to_response(
            'create_user.html', context_instance=RequestContext(request))

    def post(self, request):
        """POST method for signup."""
        first_name = request.POST['first_name']

        registration = request.POST['registration']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        cpf = request.POST.get('cpf')
        gender = request.POST.get('gender')
        confirm_password = request.POST['password2']

        print(confirm_password)
        print(password)

        if password == confirm_password:

            new_user = InspecUser()
            new_user.username = username
            new_user.email = email
            new_user.password = password
            new_user.first_name = first_name
            new_user.user_cpf = cpf
            new_user.user_gender = gender
            new_user.user_registration = registration
            new_user.set_password(password)

            new_user.save()
            response = redirect('/login/')
        else:
            response = redirect('/signup/')

        return response
