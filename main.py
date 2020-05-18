# !/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv, exit
from srcs.input import input_start

def usage():
    print("USAGE : ./main.py\nInstructions will be displayed "\
    "on the screen. For more information, please, take a look "\
    "at the README.md file or the documentation/ directory")
    return 1

if __name__ == '__main__':
    if len(argv) != 1:
        exit(usage())
    print("Welcome to the Survey monitor !")
    exit(input_start())