from flask import Flask
from flask_ask import Ask, statement, question, session
import json, requests, time, unidecode

# JSON to interact with the reddit api
# request to interact
# time to space between the reddit api
# unidecode for texts that python does not know how to use

# Method to get headlines
# use decerators like app.launch and app.route ask.intent("YesIntent")

# Create Flask
app = Flask(__name__)
ask = Ask(app,"/reddit_reader")

def get_headlines():
    user_pass_dict = {'user': 'kooklall',
                 'passwd': 'langan1107',
                 'api_type': 'json'}
    sess = requests.Session()
    sess.headers.update({'User-Agent': 'Testing Alexa' })
    # Login to reddit
    sess.post('https://www.reddit.com/api/login', data=user_pass_dict)
    time.sleep(1)
    # Change worldnews to anything
    url = 'https://reddit.com/r/nintendo-switch/.json?limit=10'
    html = sess.get(url)
    data = json.loads(html.content.decode('utf-8'))
    titles = [unidecode.unidecode(listing['data']['title']) for listing in data['data']['children']]
    titles = '\n'.join([i for i in titles])
    return titles

print(get_headlines())
# Set route
@app.route('/')
def homepage():
    return 'Hi, how are you doing today?'

# On launch Alexa will greet with @ask.launch:
@ask.launch
def start_skill():
    welcome_message = 'Hello there, would you like to hear the news?'
    return question(welcome_message)

# Alexa responses
@ask.intent("YesIntent")
def share_headline():
    headlines = get_headlines()
    headline_message = 'The current world news are {}'.format(headlines)
    return statement(headline_message)

@ask.intent('NoIntent')
def no_headline():
    text = 'Ok goodbye...let me know if you need anything else'
    return statement(text)

if __name__ == '__main__':
    app.run(debug=True)
    
