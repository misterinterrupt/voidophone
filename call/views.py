from django.http import HttpResponse
import twilio
import scapi

MP3_URL = 'http://soundcloud.com/misterinterrupt/spectralis/download'

def index(request):
    return HttpResponse("Call Index")
    
def listen(request):
    response = twilio.Response()
    response.append(twilio.Say("You have reached the void. Now listen to spectralis by misterinterrupt", voice=twilio.Say.WOMAN, 
        language=twilio.Say.ENGLISH))
    response.addPlay(MP3_URL)
    return HttpResponse(response)