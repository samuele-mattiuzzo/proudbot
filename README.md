# Proudbot

### Requirements

- Python 3.x.x

### Installation and setup (Linux/Mac)

1. Clone the repository
2. cd into the cloned directory
3. Create a virtualenv `python3 -m venv .env`
4. Activate the virtualenv `source .env/bin/activate`
5. Install the dependencies `python3 -m pip install -r requirements.txt`
6. Create a local file `config.ini` matching the format of config.ini.example in root. Add your tokens, etc. here.
7. Run the python script `python3 slackbot.py`

### Installation and setup (Windows)

1. Clone the repository
2. cd into the cloned directory
3. Create a virtualenv `python -m venv .env`
4. Activate the virtualenv `cd .env/bin/Scripts/` first then run `activate`
5. Go back to the main project folder and install the dependencies `python -m pip install -r requirements.txt`
6. Create a local file `config.ini` matching the format of config.ini.example in root. Add your tokens, etc. here.
7. Run the python script `python slackbot.py`
