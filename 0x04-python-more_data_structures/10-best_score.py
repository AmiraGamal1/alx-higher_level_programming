#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary and isinstance(a_dictionary, dict):
        sort_dict = sorted(a_dictionary.keys())
        return sort_dict[-1]
    return None
