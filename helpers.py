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
    try:
        with open(file) as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        return None

def get_random_quote():
    all_quotes = read_json_file("quotes.json")
    
    if all_quotes:
        random_quote_id = random.randrange(len(all_quotes))
        random_quote = all_quotes[random_quote_id]
        return random_quote
    return {"text": "No quotes found"}