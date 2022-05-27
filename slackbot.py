import configparser
import os

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Bot and App tokens
SLACK_BOT_TOKEN = None
SLACK_APP_TOKEN = None

conf = configparser.ConfigParser()
conf.read('config.ini')
SLACK_APP_TOKEN = str(conf.get('ACCESS', 'SLACK_APP_TOKEN'))
SLACK_BOT_TOKEN = str(conf.get('ACCESS', 'SLACK_BOT_TOKEN'))

# Initializes your app with your bot token and socket mode handler
app = App(token=SLACK_BOT_TOKEN)

if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()
