"""
********************************************************************************
* Name: urls.py
* Author: Nathan Swain
* Created On: 2014
* Copyright: (c) Brigham Young University 2014
* License: BSD 2-Clause
********************************************************************************
"""
from django.conf.urls import patterns, url, include

service_urls = [
    url(r'^$', 'tethys_services.views.wps_service', name='wps_service'),
    url(r'^process/(?P<identifier>[\w._-]+)/$', 'tethys_services.views.wps_process', name='wps_process')
]

urlpatterns = patterns('',
    url(r'^datasets/$', 'tethys_services.views.datasets_home', name='datasets_home'),
    url(r'^wps/$', 'tethys_services.views.wps_home', name='wps_home'),
    url(r'^wps/(?P<service>[\w._-]+)/', include(service_urls)),
)