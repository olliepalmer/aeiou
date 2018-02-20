from google.cloud import translate
import json
import random
translate_client = translate.Client()
target = 'en'
phrase = ''
letters = ['a','e','i','o','u',' ']

file_path = '/Users/o/Dropbox/Apps/ifttt/translationbot/' # this is the path to the dropbox folder i have set up to tweet via IFTTT (iftt.com)


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






def tweet():
	the_data = translateJibberish()
	data = json.dumps(the_data)
	json_to_python = json.loads(data)

	the_text = json_to_python['translatedText']
	f = open(file_path+the_text+".txt", "w+")
	f.write(str(json_to_python))
	f.close()
	# nb this is saved into dropbox
	# and will be tweeted via ifttt
	# using workflow which tweet the title of every
	# new text file within a specified folder 


tweet()