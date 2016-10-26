from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^dashboard', views.index, name="index"),
    url(r'^add$', views.add, name="additem"),
    url(r'^wish_items/create$', views.create, name="createitem"),
    url(r'^wish_items/(?P<id>\d+)$', views.show, name="show"),
    url(r'^wish_items/delete/(?P<id>\d+)$', views.delete, name="delete"),
    url(r'^remove/(?P<id>\d+)$', views.remove, name="remove"),
    url(r'^join/(?P<id>\d+)$', views.join, name="join"),
]
