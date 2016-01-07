from urllib2 import Request, urlopen, URLError
import json

WORDS = ["TRANSLATE"]

def handle(text, mic, profile):
    mic.say('What word?')
    word = mic.activeListen()
    mic.say('To what Language?')
    language = mic.activeListen()
    result = getTranslation(language,word)
    mic.say(result)

def getTranslation(toLang,text):
    key = ""
    if toLang == 'German':
        lang_code = 'de'
    elif toLang == 'Spanish':
        lang_code = 'es'
    request = Request('https://translate.yandex.net/api/v1.5/tr.json/translate?key='+key+'='+text+'&lang=en-'+lang_code)
    try:
        response = urlopen(request)
        data = json.load(response)
        print data['text']
        return data['text']
    except URLError, e:
    	mic.say("Unable to reach API");
        print 'Unable to hit URL', e

