# !/usr/bin/env python
# -*- coding: utf-8 -*-

from srcs.survey import Survey

class SurveyController:
    def __init__(self):
        self._surveys = []
        self._id_counter = 0

    def print_help(self):
        print("HELP")
        return self.input_start()

    def new_survey(self):
        print("Let's create a new survey !")
        survey = Survey(self._id_counter)
        self._id_counter += 1
        self._surveys.append(survey)
        return self.input_start()

    def exit_input(self):
        print("Thanks a lot and see you soon !")
        return 0

    def add_question(self):
        new_question = input("Which question do you wanna add ? : ")
        print("new question added : " + new_question)
        return self.input_start()

    def get_survey(self):
        print("Here is the surveys you want")
        return self.input_start()

    def survey_list(self):
        print("Here are all the surveys")
        return self.input_start()

    def survey_stats(self):
        print("Here are the stats of the survey you want")
        return self.input_start()

    def question_stats(self):
        print("Here are the stats for the question you want")
        return self.input_start()

    def new_survey_response(self):
        print("Here is a new survey response")
        self.survey_list()
        self._surveys[0].new_response()
        return self.input_start()

    def get_survey_response(self):
        print("Here are all the survey responses")
        return self.input_start()

    def input_start(self):
        possibilities = {
        "new survey": self.new_survey,
        "get survey": self.get_survey,
        "list survey": self.survey_list,
        "survey list": self.survey_list,
        "add question": self.add_question,
        "survey stats": self.survey_stats,
        "question stats": self.question_stats,
        "survey statistics": self.survey_stats,
        "question statistics": self.question_stats,
        "new survey response": self.new_survey_response,
        "get survey response": self.get_survey_response,

        "new": self.new_survey,
        "help": self.print_help,
        "exit": self.exit_input,
        "list": self.survey_list,
        "add": self.add_question,

        "-h": self.print_help,
        "-e": self.exit_input,
        "-l": self.survey_list,
        "-ns": self.new_survey,
        "-gs": self.get_survey,
        "-a": self.add_question,
        "-ss": self.survey_stats,
        "-qs": self.question_stats,
        "-nsr": self.new_survey_response,
        "-gsr": self.get_survey_response,

        "h": self.print_help,
        "e": self.exit_input,
        "l": self.survey_list,
        "ns": self.new_survey,
        "gs": self.get_survey,
        "a": self.add_question,
        "ss": self.survey_stats,
        "qs": self.question_stats,
        "nsr": self.new_survey_response,
        "gsr": self.get_survey_response
        }

        request = input("what do you want ? : ")
        try:
            return possibilities[request]()
        except:
            print("bad_input ! Use \"help\" to see how to use it !")
            return self.input_start()
        return 0