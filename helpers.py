# Helper functions

import re
import json
import random

MOCK_PRIDE_FACTS_TEXT = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

def create_person_id(name):
    return name.lower().replace(" ", "_")

def create_pride_facts_button(name):
    button_id = create_person_id(name)
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

def read_file(person_id):
    try:
        with open('peoplez/' + person_id + '.md', 'r') as f:
            return f.read()
    except FileNotFoundError:
        return MOCK_PRIDE_FACTS_TEXT    

def text_matches(text, match_phrase):
    return bool(re.search(match_phrase, text, re.IGNORECASE))

def read_json_file(file):
    f = open(file)
    data = json.load(f)
    print(data)
    f.close()
    return data

def get_random_quote():
    all_quotes = read_json_file("quotes.json")
    random_quote_id = random.randrange(0, len(all_quotes) - 1)
    print(random_quote_id)
    random_quote = all_quotes[random_quote_id]
    return random_quote