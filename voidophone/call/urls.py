from django.conf.urls.defaults import *
from voidophone.call.views import index, listen, record
urlpatterns = patterns('',
    #home
    url(r'^/?$', index, name='call_index'),
    url(r'^/process_index/?$', process_index, name='call_process_index')
    url(r'^listen/?$', listen, name='call_listen'),
    url(r'^record/?$', record, name='call_record')
)
