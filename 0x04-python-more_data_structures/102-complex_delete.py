#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary.keys())

    for dic_val in list_keys:
        if value == a_dictionary.get(dic_val):
            del a_dictionary[dic_val]

    return (a_dictionary)
