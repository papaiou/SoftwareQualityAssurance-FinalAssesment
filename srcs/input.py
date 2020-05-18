# !/usr/bin/env python
# -*- coding: utf-8 -*-

def print_help():
    print("HELP")
    return input_start()

def new_survey():
    print("Let's start a new survey !")
    return input_start()

def exit_input():
    print("Thanks a lot and see you soon !")
    return 0

def input_start():
    possibilities = {
    "help": print_help,
    "-h": print_help,
    "h": print_help,
    "new survey": new_survey,
    "new Survey": new_survey,
    "new": new_survey,
    "-n": new_survey,
    "n": new_survey,
    "exit": exit_input,
    "-e": exit_input,
    "e": exit_input,
    }

    request = input("what do you want ? : ")
    try:
        return possibilities[request]()
    except:
        print("bad_input !")
        return input_start()
    return 0