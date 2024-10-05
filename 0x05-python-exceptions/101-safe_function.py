#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        x = fct(*args)
        return x
    except Exception as e:
        print("Exception: {}".format(e.args[0]), file=sys.stderr)
        return None
