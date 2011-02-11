from django.conf.urls.defaults import *
from call.views import index
urlpatterns = patterns('',
    #home
    url(r'^/?$', index, name='call_index'),
)
