from django.conf.urls.defaults import *
from call.views import index, listen
urlpatterns = patterns('',
    #home
    url(r'^/?$', index, name='call_index'),
    url(r'^listen/?$', listen, name='call_listen'),
)
