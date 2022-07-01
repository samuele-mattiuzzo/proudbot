# Helper functions

import re
import json
import random

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

def read_md_file(person_id):
    try:
        with open('peoplez/' + person_id + '.md', 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "No information found"

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