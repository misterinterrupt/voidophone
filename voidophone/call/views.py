from django.http import HttpResponse
from django.core.urlresolvers import reverse
import twilio
import scapi

MP3_URL = 'http://soundcloud.com/misterinterrupt/02-suffocation-erruption-mp3/stream'

def index(request):
    r = twilio.Response()
    r.append(twilio.Say('rinresidbydvetemYochuharuptatvheoieter', voice=twilio.Say.MAN, 
        language=twilio.Say.ENGLISH, loop=3))
    r.append(twilio.Say('You have reached the void by misterinterrupt.', voice=twilio.Say.WOMAN, 
        language=twilio.Say.ENGLISH))
    g = r.append(twilio.Gather(action='call_process_index', method='GET', numDigits=10))
    g.append(twilio.Say('Press 1 to listen or press 2 to record'))
    return HttpResponse(r.__repr__())

def process_index(request):
    r = twilio.Response()
    if request.GET['Digits'] == 1:
        r.append(twilio.Redirect(reverse('call_listen')))
    elif request.GET['Digits'] == 2:
        r.append(twilio.Redirect('call_record'))
    else:
        r.append(twilio.Redirect('call_index'))
    r.append(twilio.Say('Ok.'))
    return HttpResponse(r.__repr__())

def listen(request):
    r = twilio.Response()
    r.addPlay(MP3_URL)
    return HttpResponse(r)
    
def record(request):
    r = twilio.Response()
    r.append(twilio.Say('Please record a sound for oblivion.', voice=twilio.Say.WOMAN, 
        language=twilio.Say.ENGLISH))
    r.append(twilio.Record())
    return HttpResponse(r)