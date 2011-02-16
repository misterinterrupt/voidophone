from django.conf.urls.defaults import *
from voidophone.call.views import index, listen, record
urlpatterns = patterns('',
    #home
    (r'^/?$', index, name='call_index'),
    (r'^listen/?$', listen, name='call_listen'),
    (r'^record/?$', record, name='call_record')
)
