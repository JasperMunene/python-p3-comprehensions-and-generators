#!/usr/bin/env python3

def return_evens(num_list):
    evens = list()
    for n in num_list:
        if n % 2 == 0:
            evens.append(n)
    return evens
    pass

def make_exclamation(sentence_list):
    text = list()
    for n in sentence_list:
        n = f"{n}!"
        text.append(n)
    return text
    pass