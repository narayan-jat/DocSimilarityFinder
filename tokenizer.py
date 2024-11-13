"""
The Tokenizer module provides a function to tokenize string content, extracting tokens and their frequencies
from the <TITLE> and <TEXT> sections of a document. Tokens are returned in the form of a dictionary, where each
token is a key and its frequency in the document is the value.

Author: Narayan Jat
Date: 22 April 2024
"""


def tokenize(content):
    """
    Tokenizes the content by extracting alphanumeric and underscore sequences as tokens from the <TITLE> and <TEXT>
    sections.

    Args:
    - content (str): The content of a document.

    Returns:
    - tokens (dict): A dictionary containing tokens as keys and their frequencies as values,
                     including a meta-information key 'TOTAL_TOKENS' for total token count.
    """
    # Initializing pointers and accumulators.
    tokens = {}
    total_tokens = 0
    tag_start = False
    content_start = False
    word = ""
    for char in content:
        char = char.lower()
        if char == "<":
            if len(word) > 0:       # Handling the case for addition of last word to tokens before tag ends.
                total_tokens += 1
                add_token(tokens, word)
            tag_start = True
        elif char == ">":
            tag_start = False
            if word == 'title' or word == "text":
                content_start = True
            else:
                content_start = False
            word = ""
        elif tag_start:
            word += char
        elif content_start:
            if char.isalnum() or char == '_':
                word += char
            elif len(word) > 0:
                add_token(tokens, word)
                total_tokens += 1
                word = ""
    tokens["TOTAL_TOKENS"] = total_tokens           # Meta information for tokens to improve efficiency.
    return tokens


def add_token(tokens, word):
    """
    This helper function adds a token to the token dictionary 'tokens' or increments its frequency if it already exists.

    Args:
    - tokens (dict): The dictionary containing tokens as keys and their frequencies as values.
    - word (str): The token to add or update in the dictionary.
    """
    if word in tokens:
        tokens[word] += 1
    else:
        tokens[word] = 1
