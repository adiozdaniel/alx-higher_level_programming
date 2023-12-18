#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        output = a/b
    except:
        output = None
    finally:
        print("Inside output: {}".format(output))
    return (output)
