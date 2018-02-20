# aeiou

This is a quick, messy bot which plays with Google Translate's tendency to mis-interpret strings of vowels as Hawaiian phrases, as documented [here](http://languagelog.ldc.upenn.edu/nll/?p=36753). It currently spits out to [this Twitter account](https://twitter.com/hawaiian_wisdom).

![](https://www.dropbox.com/s/k9b8kwtqyyk6pts/Screenshot%202018-02-20%2015.02.28.png?dl=1)

This is the first bot I've built in a while, so I'm a bit rusty. It is quick and dirty, so doesn't automate everything. The basic premise is:

- A Python script generates a random string of 250 vowels (a,e,i,o,u) and spaces. It connects to the Google Translate API and receives a translation
- The returned translation JSON data is saved into a text file in my Dropbox. The title of the file is the translation.
- An [If This Then That](http://ifttt.com) Applet scans the folder in my Dropbox for new text files, tweeting the file name. 

So, yes, this is a hacky, messy workaround. I will tidy it up and make a decent workflow at some point, but I just wanted to see how quickly I could make a bot to react to an article I'd read.

Drawbacks of this approach:

- It works from my local machine, running Python in a virtual environment with the Google Translate API installed. It only tweets when the script is run, which is currently manual. (In fact, I'm working from home at the moment so just running it via the following Terminal command: <code>for i in {1..100}; do python /Users/o/Documents/github-root/bots/aeiou/translate_and_tweet.py; sleep 10m; done</code>
- It uses IFTT, which is sometimes slow to run
- It's just a bit messy and localised
- It requires a paid Google Translate API account. It only costs a couple of Euro per month to run, but still, shame there isn't a free way.

## Things I need to do

- Make the code easily executable
- Come up with a good project name
- Rewrite this description

## How to make this work on your machine

My computer is a flipping mess. 

1. Create a new folder with project 'aeiou' (or whatever you want to call it), clone this directory into it.
2. . Create virtual environment with python 3.6. NB – I have to do this in a few stages because my default Python is Anaconda, and it messes up installing Python 3.6 with pip (this process creates a venv *without* pip then installs pip). My venv is called <code>aeiou-venv</code>:
 <code>
    python3 -m venv --without-pip aeiou-venv
    source aeiou-venv/bin/activate
    curl https://bootstrap.pypa.io/get-pip.py | python
    deactivate
    source aeiou-venv/bin/activate
</code>
[see here for more info](https://stackoverflow.com/questions/26215790/venv-doesnt-create-activate-script-python3)

3. Install Google Cloud Translate API stuff:
<code>
    pip install --upgrade google-cloud-translate
</code>

4. Follow the instructions [here](https://cloud.google.com/translate/docs/reference/libraries) to create a service account key, and a gain a paid API access token.
Create a Google Cloud Development Project, with billing enabled for your API. More info [here](https://cloud.google.com/translate/docs/quickstart). Make sure to download the JSON file and save it as 'credentials.json' in your project root folder! *Note that when we set up a git project, we'll explicitly ignore this file.*
5. Set the environment variable GOOGLE_APPLICATION_CREDENTIALS to the file path of the JSON file that contains your service account key (see [this page again](https://cloud.google.com/translate/docs/reference/libraries)!)
6. Run the python code 

