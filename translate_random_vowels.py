from google.cloud import translate
import json
import random
translate_client = translate.Client()
target = 'en'
phrase = ''
letters = ['a','e','i','o','u',' ']

def makePhrase():
	phrase = ''
	for i in range(250):
		phrase += random.choice(letters)
	return(phrase)

def translateJibberish():
	translation = translate_client.translate(
		makePhrase(),
		target_language=target)
	return(translation)

print (translateJibberish())