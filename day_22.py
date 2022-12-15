# Day 22: Add Under_Score

def add_hash(strs):
    if len(strs.split()) > 1:
        return '#'.join(strs.split())
    return strs

def add_underscore(strs):
    if '#' in strs:
        return strs.replace('#', '_')
    return strs

def remove_underscore(strs):
    if '_' in strs:
        return strs.replace('_', '')
    return strs
