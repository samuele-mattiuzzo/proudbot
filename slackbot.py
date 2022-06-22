#!/usr/bin/python3
import configparser
import datetime
import logging

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_bolt.context.say import say

log = logging.getLogger(__name__)

# Bot and App tokens
SLACK_BOT_TOKEN = None
SLACK_APP_TOKEN = None

conf = configparser.ConfigParser()
conf.read('config.ini')
SLACK_APP_TOKEN = str(conf.get('ACCESS', 'SLACK_APP_TOKEN'))
SLACK_BOT_TOKEN = str(conf.get('ACCESS', 'SLACK_BOT_TOKEN'))

# Initializes your app with your bot token and socket mode handler
app = App(token=SLACK_BOT_TOKEN)

## Listeners
@app.command("/proudbot")
def dispatcher(ack, say, body):
    text = body["text"]
    user_id = body["user_id"]
    if text == "hello":
        message = message_hello(user_id)
    elif text == "when is pride parade?":
        message = message_pride_parade()
    elif text == "pride facts":
        # TODO: this needs a bit or refactoring
        message = ""
        message_pride_facts(user_id, say)
    else:
        message = message_helper(user_id)
    if message != "": 
        say(message)
    ack()
    

# Listens to incoming messages that contain "help"
def message_helper(user_id):
    return f"The following commands are available\n" + \
            "`/proudbot hello` - Get a personalised greeting from ProudBot\n" + \
            "`/proudbot when is pride parade?` - Get the date of the next pride parade\n" + \
            "`/proudbot pride facts` - Get facts about various LGBTQ+ advocates and activists\n"

# Listens to incoming messages that contain 'when is pride parade'
def message_pride_parade():
    pride_day = datetime.date(2022,7,2)
    message = "The London Pride parade is on {}/{}/{}".format(
        pride_day.day,
        pride_day.month,
        pride_day.year
    )
    return message

# Listens to incoming messages that contain 'hello'
def message_hello(user_id):
    return f"Hey there <@{user_id}>! :partyparrot:"

# Listens to incoming messages that contain 'pride facts'
def message_pride_facts(user_id, say):
    say(
        blocks = [
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"Hey there <@{user_id}>!"},
            },
            {
                "type": "actions",
                "block_id": "actionblock789",
                "elements": [
                    create_pride_facts_button("Angelica Ross"),
                    create_pride_facts_button("Anna Arriola"),
                    create_pride_facts_button("Edith Windsor"),
                    create_pride_facts_button("Eudora Welty"),
                    create_pride_facts_button("James Baldwin"),
                    create_pride_facts_button("John Amaechi"),
                    create_pride_facts_button("Justin Fashnu"),
                    create_pride_facts_button("Langston Hughes"),
                    create_pride_facts_button("Leanna Pittsford"),
                    create_pride_facts_button("Lynn Conway"),
                    create_pride_facts_button("Ma Rainey"),
                    create_pride_facts_button("Marsh P Johnson"),
                    create_pride_facts_button("Pearl Alcock"),
                    create_pride_facts_button("Sister Rosetta Tharpe"),
                    create_pride_facts_button("Sofia Kovalevskaya"),
                    create_pride_facts_button("Sylvester"),
                    create_pride_facts_button("Zanele Muholi"),
                ]
            }
        ]
    )

def create_pride_facts_button(name):
    button_id = create_id(name)
    button = {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": f"Tell me about {name}"
                },
                "style": "primary",
                "value": f"{button_id}_info",
                "action_id": f"{button_id}_info"
            }
    return button

def create_id(string):
    return string.lower().replace(" ", "_")

## Actions

mock_pride_facts_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

# TODO: try to make this a dynamic function that just takes a person and then displays some info about the person instead of having multiple functions
@app.action("angelica_ross_info")
def angelica_ross_info_click(body, ack, say):
    log.debug("OK")
    ack()
    info_text = mock_pride_facts_text
    say(info_text)

@app.action("anna_arriola_info")
def anna_arriola_info_click(body, ack, say):
    ack()
    info_text = mock_pride_facts_text
    say(info_text)

@app.action("edith_windsor_info")
def edith_windsor_info_click(body, ack, say):
    ack()
    info_text = mock_pride_facts_text
    say(info_text)

@app.action("eudora_welty_info")
def eudora_welty_info_click(body, ack, say):
    ack()
    info_text = mock_pride_facts_text
    say(info_text)

@app.action("james_baldwin_info")
def james_baldwin_info_click(body, ack, say):
    ack()
    info_text = mock_pride_facts_text
    say(info_text)

@app.action("john_amaechi_info")
def john_info_click(body, ack, say):
    ack()
    info_text = "John Uzoma Ekwugha Amaechi, OBE (/əˈmeɪtʃi/; born 26 November 1970) is a British-American psychologist, consultant and former professional basketball player. He played college basketball at Vanderbilt and Penn State, and professional basketball in the National Basketball Association (NBA). Amaechi also played in France, Greece, Italy, and the United Kingdom. Since retiring from basketball, Amaechi has worked as a psychologist and consultant, establishing his company Amaechi Performance Systems."
    say(info_text)    

@app.action("justin_fashnu_info")
def justin_fashnu_info_click(body, ack, say):
    ack()
    info_text = mock_pride_facts_text
    say(info_text)

@app.action("langston_hughes_info")
def langston_hughes_info_click(body, ack, say):
    ack()
    info_text = mock_pride_facts_text
    say(info_text)

@app.action("leanna_pittsford_info")
def leanna_pittsford_info_click(body, ack, say):
    ack()
    info_text = mock_pride_facts_text
    say(info_text)

@app.action("lynn_conway_info")
def lynn_conway_info_click(body, ack, say):
    ack()
    info_text = mock_pride_facts_text
    say(info_text)

@app.action("ma_rainey_info")
def ma_rainey_info_click(body, ack, say):
    ack()
    info_text = mock_pride_facts_text
    say(info_text)

@app.action("marsh_p_johnson_info")
def marsh_p_johnson_info_click(body, ack, say):
    ack()
    info_text = mock_pride_facts_text
    say(info_text)

@app.action("pearl_alcock_info")
def pearl_alcock_info_click(body, ack, say):
    ack()
    info_text = mock_pride_facts_text
    say(info_text)

@app.action("sister_rosetta_tharpe_info")
def sister_info_click(body, ack, say):
    ack()
    info_text = 'Sister Rosetta Tharpe (born Rosetta Nubin, March 20, 1915 – October 9, 1973)[2] was an American singer and guitarist. She first gained popularity in the 1930s and 1940s with her gospel recordings, characterized by a unique mixture of spiritual lyrics and electric guitar. She was the first great recording star of gospel music, and was among the first gospel musicians to appeal to rhythm and blues and rock and roll audiences, later being referred to as "the original soul sister"' 
    say(info_text)

@app.action("sofia_kovalevskaya_info")
def sofia_kovalevskaya_info_click(body, ack, say):
    ack()
    info_text = mock_pride_facts_text
    say(info_text)

@app.action("sylvester_info")
def sylvester_info_click(body, ack, say):
    ack()
    info_text = mock_pride_facts_text
    say(info_text)

@app.action("zanele_muholi_info")
def zanele_muholi_info_click(body, ack, say):
    ack()
    info_text = mock_pride_facts_text
    say(info_text)   

#Handle messages that are not for proudbot
@app.event("message")
def handle_message_events(body, logger):
    pass
          

if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()
