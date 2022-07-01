#!/usr/bin/python3
import configparser
import datetime

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_bolt.context.say import say

from helpers import (create_person_id, create_pride_facts_button, read_file,
                     text_matches)

# Bot and App tokens
SLACK_BOT_TOKEN = None
SLACK_APP_TOKEN = None

conf = configparser.ConfigParser()
conf.read('config.ini')
SLACK_APP_TOKEN = str(conf.get('ACCESS', 'SLACK_APP_TOKEN'))
SLACK_BOT_TOKEN = str(conf.get('ACCESS', 'SLACK_BOT_TOKEN'))


# Initializes your app with your bot token and socket mode handler
app = App(token=SLACK_BOT_TOKEN)


# Listeners
@app.command("/proudbot")
def dispatcher(ack, say, body):
    text = body["text"]
    user_id = body["user_id"]
    message = ''
    if text_matches(text, "hello"):
        message = message_hello(user_id)
    elif text_matches(text, "when is pride parade?"):
        message = message_pride_parade()
    elif text_matches(text, "pride facts"):
        message = message_pride_facts(user_id, say)
    elif text_matches(text, "pride quote"):
        message = message_pride_quote()
    elif message == '':
        # shows the helper
        message = message_helper(user_id)
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
    pride_day = datetime.date(2022, 7, 2)
    message = "The London Pride parade is on {}/{}/{}".format(
        pride_day.day,
        pride_day.month,
        pride_day.year
    )
    return message


# Listens to incoming messages that contain 'pride quote'
def message_pride_quote():
    return {"blocks": [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "\n>_Lorem ipsum dolor sit amet, consectetur adipiscing elit_\n>\nby *John Doe*"
            }
        }
    ]}


# Listens to incoming messages that contain 'hello'
def message_hello(user_id):
    return f"Hey there <@{user_id}>! :partyparrot:"


# Listens to incoming messages that contain 'pride facts'
def message_pride_facts(user_id, say):
    return {"blocks": [
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
    ]}


# Actions
@app.action("angelica_ross_info")
@app.action("anna_arriola_info")
@app.action("edith_windsor_info")
@app.action("eudora_welty_info")
@app.action("james_baldwin_info")
@app.action("john_amaechi_info")
@app.action("sister_rosetta_tharpe_info")
@app.action("langston_hughes_info")
@app.action("justin_fashnu_info")
@app.action("leanna_pittsford_info")
@app.action("lynn_conway_info")
@app.action("ma_rainey_info")
@app.action("marsh_p_johnson_info")
@app.action("pearl_alcock_info")
@app.action("sofia_kovalevskaya_info")
@app.action("sylvester_info")
@app.action("zanele_muholi_info")
def person_info_click(body, ack, say):
    ack()
    person_id = body['actions'][0]['value']
    info_text = read_file(person_id)
    say(info_text)


# Handle messages that are not for proudbot
@app.event("message")
def handle_message_events(body, logger):
    pass


if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()
