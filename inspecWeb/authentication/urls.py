"""Urls for authentication app."""

from django.conf.urls import url

from .views import Login, SignUp, Logout, Home, Index

urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^index/', Index.as_view(), name='index'),
    url(r'^login/', Login.as_view(), name='login'),
    url(r'^signup/', SignUp.as_view(), name='signin'),
    url(r'^logout/', Logout.as_view(), name='logout'),
]
