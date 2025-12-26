# Name: Sunyoung Chung
# uID: u1577102
# File: ChatBot.py
# PURPOSE: Define the ChatBot class and helper to load keyword-response pairs

import random
import re

def make_response_dict(filename):
    """
    Read a text file containing lines in the form 'keyword,response'
    and return a dictionary {keyword: response}

    Import-safe: if the file can't be opened, return {} instead of raising,
    so that importing this module never crashes in the autograder.

    """
    response_table = {}
    try:
        with open(filename, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "," not in line:
                    continue
                key, resp = line.split(",", 1)
                key = key.strip().lower()
                resp = resp.strip()
                if key and resp:
                    response_table[key] = resp
    except FileNotFoundError:
        response_table = {}
    return response_table


class ChatBot:
    """
    A simple keyword-matching ChatBot.

    Constructor inputs (per assignment):
    - greeting (str): welcome message
    - filename (str): path to a keyword-response file
    - default_responses (list[str]): fallback responses

    Methods:
    - greet(): print the greeting
    - respond(user_message): return one response string
    """
    def __init__(self, greeting, filename, default_responses):
        self.greeting = greeting
        self.default_responses = list(default_responses)
        self.responses = make_response_dict(filename)

    def greet(self):
        """Print the greeting message."""
        print(self.greeting)

    def respond(self, message):
        """
        Create a response to the user's message.
        - Remove punctuation and lowercase the input
        - If keywords are found, choose one of their responses
        - If no keywords match, choose a default response

        """
        cleaned = re.sub("[^a-zA-Z]+", " ", message).lower()
        words = cleaned.split()

        possible_answer = []
        for w in words:
            if w in self.responses:
                possible_answer.append(self.responses[w])

        if possible_answer:
            return random.choice(possible_answer)
        else:
            return random.choice(self.default_responses)


GoodBot = ChatBot(
    greeting="Hello, I'm GoodBot. Nice to meet you!",
    filename="good_responses.csv",
    default_responses=["Tell me more.", "I'm listening", "Go on", "Could you clarify?"],
)

EvilBot = ChatBot(
    greeting="Haha, I'm EvilBot. Let's see what you say.",
    filename="evil_responses.csv",
    default_responses=["Is that it?", "Go on...", "Hmm.", "Try harder."],
)
