import os, json, random
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"
from google.cloud import translate
ancient_wisdom = translate.Client()
letters = ['a','e','i','o','u',' ']

def impart_wisdom():
	input_phrase = '' # reset the phrase
	for i in range(random.randint(150,250)):
		input_phrase += random.choice(letters)
	translation = ancient_wisdom.translate(input_phrase, target_language='en') # this sends google our phrase and receives their translation
	advice = json.dumps(translation) # but the translation in in a format called json, which sounds just like 'jason' but is a way of storing data
	make_legible = json.loads(advice) # we need to get data out of the json format and into plain text
	return(make_legible['input'],make_legible['translatedText'])

wisdom = impart_wisdom()
print(wisdom[0],'/',wisdom[1])
