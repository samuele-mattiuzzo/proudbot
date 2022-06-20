#!/usr/bin/python3
import configparser
import datetime

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_bolt.context.say import say

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

# Listens to incoming messages that contain "hello"
@app.command("/proudbot")
def message_hello(ack, say, body):
    text = body["text"]
    user_id = body["user_id"]
    if text == "hello":
        # say() sends a message to the channel where the event was triggered
        say(f"Hey there <@{user_id}>! :partyparrot:")
    else:
        message = message_helper(user_id)
        say(message)
    ack()
    

# Listens to incoming messages that contain "help"
# @app.message("help")
def message_helper(user_id):
    return f"Hey there <@{user_id}>! Try these commands maybe?\n" + \
            "- hello\n" + \
            "- when is pride parade?\n" + \
            "- pride facts\n"

# Listens to incoming messages that contain 'when is pride parade'
@app.message("when is pride parade")
def message_pride_parade(message, say):
    pride_day = datetime.date(2022,7,2)
    message = "The London Pride parade is on {}/{}/{}".format(
        pride_day.day,
        pride_day.month,
        pride_day.year
    )
    say(message)

# Listens to incoming messages that contain "pride facts"
@app.message("pride facts")
def message_pride_facts(message, say):
    say(
        blocks = [
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"Hey there <@{message['user']}>!"},
            },
            {
                "type": "actions",
                "block_id": "actionblock789",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Tell me about John Amaechi"
                        },
                        "style": "primary",
                        "value": "john_info",
                        "action_id": "john_info"
                    },
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Tell me about Sister Rosetta Tharpe"
                        },
                        "style": "primary",
                        "value": "sister_info",
                        "action_id":"sister_info"
                    }
                ]
            }
        ]
    )


## Actions

@app.action("john_info")
def john_info_click(body, ack, say):
    ack()
    john_text = "John Uzoma Ekwugha Amaechi, OBE (/əˈmeɪtʃi/; born 26 November 1970) is a British-American psychologist, consultant and former professional basketball player. He played college basketball at Vanderbilt and Penn State, and professional basketball in the National Basketball Association (NBA). Amaechi also played in France, Greece, Italy, and the United Kingdom. Since retiring from basketball, Amaechi has worked as a psychologist and consultant, establishing his company Amaechi Performance Systems."
    say(john_text)

@app.action("sister_info")
def sister_info_click(body, ack, say):
    ack()
    sister_text = 'Sister Rosetta Tharpe (born Rosetta Nubin, March 20, 1915 – October 9, 1973)[2] was an American singer and guitarist. She first gained popularity in the 1930s and 1940s with her gospel recordings, characterized by a unique mixture of spiritual lyrics and electric guitar. She was the first great recording star of gospel music, and was among the first gospel musicians to appeal to rhythm and blues and rock and roll audiences, later being referred to as "the original soul sister"' 
    say(sister_text)

if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()
