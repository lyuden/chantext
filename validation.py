'''
Filtering and validation
'''

def filter_search(search_words):
    return [ w.lower() for w in search_words if w != '']