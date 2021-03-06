# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from srcs.survey import Survey

class SurveyController:
    def __init__(self):
        self._surveys = []
        self._survey_names = []
        self._id_counter = 0
        print("Welcome to the Survey monitor !")

    def print_help(self):
        print("Welcome to the Survey monitor help. Here, you will find every possible commands to manage our Survey monitor :")
        print("\ta|-a|add|add question : Permanently add a question to our fake database.")
        print("\te|-e|exit : Exit the monitor and the program.")
        print("\tgs|-gs|get survey : Display all informations available about a Survey.")
        print("\tgsr|-gsr|get survey response: Display all informations available about a Survey Response.")
        print("\th|-h|help : Print this help panel.")
        print("\tl|-l|list|list survey|survey list: List all Surveys created.")
        print("\tns|-ns|new survey : Create a new Survey.")
        print("\tnsr|-nsr|new survey response: Create a new Survey Response.")
        print("\tss|-ss|survey stats|survey statistics : Display all statistics available about a Survey.")
        print("\tqs|-qs|question stats|question statistics : Display all statistics available about a question.")
        return self.input_start()

    def new_survey(self):
        print("Let's create a new survey !")
        survey = Survey(self._id_counter, self._survey_names)
        self._id_counter += 1
        self._surveys.append(survey)
        self._survey_names.append(survey._name)
        return self.input_start()

    def exit_input(self):
        print("Thanks a lot and see you soon !")
        return 0

    def add_question(self):
        new_question = ""
        while not new_question:
            new_question = input("Which question do you wanna add ? : ")

        data = open(os.path.dirname(__file__) + "/.database.txt", "r")

        for line in data:
            if new_question == line[:-1]:
                print("Question already in the database !")
                data.close()
                return self.input_start()
        with open(os.path.dirname(__file__) + "/.database.txt", 'a') as f:
            f.write(new_question + "\n") 
        print("new question permenently added : " + new_question)
        return self.input_start()

    def get_survey(self):
        if self._surveys == []:
            print("No surveys have been created !")
            return self.input_start()
        print("Here are all surveys you had created : ")
        for survey in self._surveys:
            print(str(survey._id + 1) + " : " + survey._name)
        choice = 0
        while choice == 0:
            number = input("Which survey do you want to see ? : ")
            if not number.isdigit() or int(number) < 1 or int(number) > len(self._surveys):
                print("Please enter a number between 1 and " + str(len(self._surveys)) + ".")
                continue
            choice = int(number)
        choice -= 1
        print("Here are all informations about this survey :")
        print("Name : " + self._surveys[choice]._name)
        print("ID : " + str(self._surveys[choice]._id))
        print("Number of responses : " + str(self._surveys[choice]._id_response))
        print("Number of questions : " + str(self._surveys[choice]._nb_questions))
        print("Questions :")
        i = 0
        for question in self._surveys[choice]._questions:
            print("Question n°" + str(i + 1) + " : " + question)
            i += 1
        return self.input_start()

    def survey_list(self):
        if self._surveys == []:
            print("No surveys have been created !")
            return self.input_start()
        print("Here are all surveys you had created : ")
        for survey in self._surveys:
            print(str(survey._id + 1) + " : " + survey._name)
        return self.input_start()

    def survey_stats(self):
        if self._surveys == []:
            print("No surveys have been created !")
            return self.input_start()
        print("Here are all surveys you had created : ")
        for survey in self._surveys:
            print(str(survey._id + 1) + " : " + survey._name)
        choice = 0
        while choice == 0:
            number = input("Which survey do you want to see statistics ? : ")
            if not number.isdigit() or int(number) < 1 or int(number) > len(self._surveys):
                print("Please enter a number between 1 and " + str(len(self._surveys)) + ".")
                continue
            choice = int(number)
        choice -= 1
        if self._surveys[choice]._id_response == 0:
            print("No surveys response have been created for this survey !")
            return self.input_start()
        self._surveys[choice].display_stats()
        return self.input_start()

    def question_stats(self):
        if self._surveys == []:
            print("No surveys have been created !")
            return self.input_start()
        print("Here are all surveys you had created : ")
        for survey in self._surveys:
            print(str(survey._id + 1) + " : " + survey._name)
        choice = 0
        while choice == 0:
            number = input("Which survey do you want to see statistics ? : ")
            if not number.isdigit() or int(number) < 1 or int(number) > len(self._surveys):
                print("Please enter a number between 1 and " + str(len(self._surveys)) + ".")
                continue
            choice = int(number)
        choice -= 1
        if self._surveys[choice]._id_response == 0:
            print("No surveys response have been created for this survey !")
            return self.input_start()
        print("Here are the questions of this survey :")
        
        i = 0
        while i < self._surveys[choice]._nb_questions:
            print(str(i + 1) + " : " + self._surveys[choice]._questions[i])
            i += 1
        question = 6
        while question == 6:
            number = input("On which question of this survey do you want to see statistics ? : ")
            if not number.isdigit() or int(number) < 1 or int(number) > self._surveys[choice]._nb_questions:
                print("Please enter a number between 1 and " + str(self._surveys[choice]._nb_questions) + ".")
                continue
            question = int(number)
        question -= 1
        self._surveys[choice].display_question_stats(question)
        return self.input_start()

    def new_survey_response(self):
        if self._surveys == []:
            print("No surveys have been created !")
            return self.input_start()
        print("Here are all surveys you had created : ")
        for survey in self._surveys:
            print(str(survey._id + 1) + " : " + survey._name)
        choice = 0
        while choice == 0:
            number = input("Which survey do you want to answer ? : ")
            if not number.isdigit() or int(number) < 1 or int(number) > len(self._surveys):
                print("Please enter a number between 1 and " + str(len(self._surveys)) + ".")
                continue
            choice = int(number)
        choice -= 1
        self._surveys[choice].new_response()
        return self.input_start()

    def get_survey_response(self):
        if self._surveys == []:
            print("No surveys have been created !")
            return self.input_start()
        print("Here are all surveys you had created : ")
        for survey in self._surveys:
            print(str(survey._id + 1) + " : " + survey._name)
        choice = 0
        while choice == 0:
            number = input("Which survey do you want to answer ? : ")
            if not number.isdigit() or int(number) < 1 or int(number) > len(self._surveys):
                print("Please enter a number between 1 and " + str(len(self._surveys)) + ".")
                continue
            choice = int(number)
        choice -= 1
        self._surveys[choice].get_response()
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