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

def add_question():
    new_question = input("Which question do you wanna add ? : ")
    print("new question added : " + new_question)
    return input_start()

def get_survey():
    print("Here is the surveys you want")
    return input_start()

def survey_list():
    print("Here are all the surveys")
    return input_start()

def survey_stats():
    print("Here are the stats of the survey you want")
    return input_start()

def question_stats():
    print("Here are the stats for the question you want")
    return input_start()

def new_survey_response():
    print("Here is a new survey response")
    return input_start()

def get_survey_response():
    print("Here are all the survey responses")
    return input_start()

def input_start():
    possibilities = {
    "new survey": new_survey,
    "get survey": get_survey,
    "list survey": survey_list,
    "survey list": survey_list,
    "add question": add_question,
    "survey stats": survey_stats,
    "question stats": question_stats,
    "survey statistics": survey_stats,
    "question statistics": question_stats,
    "new survey response": new_survey_response,
    "get survey response": get_survey_response,

    "new": new_survey,
    "help": print_help,
    "exit": exit_input,
    "list": survey_list,
    "add": add_question,

    "-h": print_help,
    "-e": exit_input,
    "-l": survey_list,
    "-ns": new_survey,
    "-gs": get_survey,
    "-a": add_question,
    "-ss": survey_stats,
    "-qs": question_stats,
    "-nsr": new_survey_response,
    "-gsr": get_survey_response,

    "h": print_help,
    "e": exit_input,
    "l": survey_list,
    "ns": new_survey,
    "gs": get_survey,
    "a": add_question,
    "ss": survey_stats,
    "qs": question_stats,
    "nsr": new_survey_response,
    "gsr": get_survey_response,
    }

    request = input("what do you want ? : ")
    try:
        return possibilities[request]()
    except:
        print("bad_input ! Use \"help\" to see how to use it !")
        return input_start()
    return 0