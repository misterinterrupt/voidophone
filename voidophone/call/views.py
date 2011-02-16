from django.http import HttpResponse
import twilio
import scapi

MP3_URL = 'replace_me.mp3'

def index(request):
    r = twilio.Response()
    r.append(twilio.Say('rinresidbydvetemYochuharuptatvheoieter', voice=twilio.Say.MAN, 
        language=twilio.Say.ENGLISH, loop=3))
    r.append(twilio.Say('You have reached the void by misterinterrupt.', voice=twilio.Say.WOMAN, 
        language=twilio.Say.ENGLISH))
    g = r.append(twilio.Gather(action='call_process_index', method='GET', numDigits=10))
    g.append(twilio.Say('Press 1 to listen or press 2 to record'))
    return HttpResponse(r)

def process_index(request):
    r = twilio.Response()
    if request.get('Digits') == 1:
        r.append(twilio.Redirect('call_listen'))
    if request.get('Digits') == 2:
        r.append(twilio.Redirect('call_record'))
    r.append(twilio.Say('Ok.'))
    return HttpResponse(r)

def listen(request):
    r = twilio.Response()
    r.addPlay(MP3_URL)
    return HttpResponse(r)
    
def record(request):
    r = twilio.Response()
    r.append(twilio.Say('Please record a sound for oblivion.', voice=twilio.Say.WOMAN, 
        language=twilio.Say.ENGLISH))
    r.append(twilio.Record())