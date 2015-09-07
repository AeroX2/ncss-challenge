#!/bin/env python3

import re

RE_TOKENS = re.compile(r'[()\\/]|[a-zA-Z]+')
POSSIBLE_TOKENS = ["N","NP","PP","S"]

def tokenize(cat):
    return RE_TOKENS.findall(cat)


def parse(tokens):
    error = recurse(tokens, False)
    return not error

def recurse(tokens, error):
    if error: return True
    try:
        if tokens[0] in POSSIBLE_TOKENS:
            tokens.pop(0)
            return False
        elif tokens[0] == "(":
            tokens.pop(0)
            error = recurse(tokens, error)
            if tokens[0] == "\\" or tokens[0] == "/":
                tokens.pop(0)
                error = recurse(tokens, error)
            else:
                return True
            if tokens[0] == ")":
                tokens.pop(0)
                return error
            return True
        else:
            return True
    except IndexError:
        return True

def is_valid(cat):
    tokens = tokenize(cat)
    return parse(tokens) and len(tokens) == 0


cat = input('Enter category: ')
while cat:
    if is_valid(cat):
        print(cat, 'is valid')
    else:
        print(cat, 'is invalid')
    cat = input('Enter category: ')

