"""Urls for authentication app."""

from django.conf.urls import url

from .views import Login, SignUp, Logout

urlpatterns = [
    url(r'^login/', Login.as_view(), name='login'),
    url(r'^signup/', SignUp.as_view(), name='signin'),
    url(r'^logout/', Logout.as_view(), name='logout'),
]
