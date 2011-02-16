from django.http import HttpResponse
import twilio
import scapi

MP3_URL = 'replace_me.mp3'

def index(request):
    response = twilio.Response()
    response.append(twilio.Say("rmYochuharuptatvheoieteinresidbydveter.", voice=twilio.Say.MAN, 
        language=twilio.Say.ENGLISH, loop=10))
    response.append(twilio.Say("You have reached the void by misterinterrupt.", voice=twilio.Say.WOMAN, 
        language=twilio.Say.ENGLISH))
    response.append(twilio.Gather())
    return HttpResponse(response)
    
def listen(request):
    response = twilio.Response()
    response.addPlay(MP3_URL)
    return HttpResponse(response)
    
def record(request):
    response = twilio.Response()
    response.append(twilio.Say('Please record a sound for oblivion.', voice=twilio.Say.WOMAN, 
        language=twilio.Say.ENGLISH))
    response.append(twilio.Record())