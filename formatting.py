# encoding: utf-8

import os
import sys
import time


def clear_screen():
    os.system(["clear", "cls"][os.name == "nt"])


def spinning_cursor():
    while True:
        for cursor in "|/-\\":
            yield cursor


def sc_use(repeat):
    spinner = spinning_cursor()
    for _ in range(repeat):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write("\b")


def drawing_msg():
    print("\n\x1b[5mDrawing...\x1b[25m ", end="")


# decorator used to block function printing to the console
def blockprinting(func):
    def func_wrapper(*args, **kwargs):
        # block all printing to the console
        sys.stdout = open(os.devnull, "w")
        # call the method in question
        value = func(*args, **kwargs)
        # enable all printing to the console
        sys.stdout = sys.__stdout__
        # pass the return value of the method back
        return value

    return func_wrapper
