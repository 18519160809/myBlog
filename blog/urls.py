from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^post/(?P<pk>\d+)/$', views.detail),
    url(r'^post/(?P<pk>\d+)/$', views.detail),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category),

]