# Day 19: Words and Elements

def count_words(strs):
    return len(strs.split())

def count_elements(strs):
    return len(strs.replace(' ', ''))
