from django.urls import path
from . import urls
from . import views



urlpatterns=[
   
    path('all_networks/', views.all_networks, name='all_networks'),
    path('networks/', views.networks, name='networks'),
    path('network_load/', views.network_load, name="network_load"),
    path('get_channels/',views.get_channels, name="get_channels"),
   
   
]