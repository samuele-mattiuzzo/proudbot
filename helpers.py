# Helper functions

import re
import requests
from bs4 import BeautifulSoup

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

def get_random_page():
    return 1

def get_random_quote_in_page(base_url, page):
    response = requests.get(str(base_url) + "?page=" + str(page))
    html_text = BeautifulSoup(response.content, "html.parser")
    print(html_text.find("h1"))

    authors = html_text.findAll("div", attrs={"class": "authorOrTitle"})
    for author in authors:
        print(author)

    quotes_in_page_html = html_text.find_all("div", attrs={"class": "quote"})

    quotes = []
    i = 0
    for quote in quotes_in_page_html:
        quote_container = quote.find("div", attrs={"class": "quoteDetails"})
        quote_text = quote_container.find("div", attrs={"class": "quoteText"})
        quote_author = quote_container.find("div", attrs={"class": "authorOrTitle"})
        quotes.append(
            {
                "text": "lorem",
                "author": quote_author
            }
        )
    # print(quotes)    
    return "OK"

def get_quote():
    quotes_url = 'https://www.goodreads.com/quotes/tag/lgbt'
    response = requests.get(quotes_url)
    statusCode = response.status_code
    htmlText = BeautifulSoup(response.text, "html.parser")
    next_button = htmlText.find("")
    get_random_quote_in_page(quotes_url, 1)

    return statusCode