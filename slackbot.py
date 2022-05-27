import configparser

SLACK_BOT_TOKEN = None
SLACK_APP_TOKEN = None

conf = configparser.ConfigParser()
conf.read('config.ini')
SLACK_APP_TOKEN = str(conf.get('ACCESS', 'SLACK_APP_TOKEN'))
SLACK_BOT_TOKEN = str(conf.get('ACCESS', 'SLACK_BOT_TOKEN'))

if __name__ == "__main__":
    print(SLACK_APP_TOKEN)
    print(SLACK_BOT_TOKEN)