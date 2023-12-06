#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary and len(a_dictionary):
        sort_dict = sorted(list(a_dictionary.keys()))
        return sort_dict[-1]
    return None
