# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from srcs.survey_response import SurveyResponse
from random import randrange

class Survey:
    def __init__(self, id, namelist):
        self._responses = []
        self._id = id
        self._id_response = 0
        self._name = ""
        self._nb_questions = 0
        self._questions = []
        while not self._name:
            self._name = input("What is the name of your new Survey? : ")
            if self.check_name(namelist) == 0:
                print("Name already used for another Survey !")
                self._name = ""
        while self._nb_questions == 0:
            number = input("How many questions do you want for the survey? : ")
            if not number.isdigit() or int(number) > 10 or int(number) < 1:
                print("Number of question must be between 1 and 10")
                continue
            self._nb_questions = int(number)
        self.new_survey()

    def check_name(self, namelist):
        for name in namelist:
            if name == self._name:
                return 0
        return 1

    def new_survey(self):
        print("Here are all questions available for the Surveys : ")
        data = open(os.path.dirname(__file__) + "/.database.txt", "r")
        i = 0
        lines = []

        for line in data:
            lines.append(line[:-1])
            print("Question " + str(len(lines)) + ": " + line[:-1])
        data.close()
        while i < self._nb_questions:
            j = 0
            repeat = False

            number = input("Which question do you want to put in your survey? : ")
            if not number.isdigit() or int(number) < 1 or int(number) > len(lines):
                print("Please enter a number between 1 and " + str(len(lines)) + ".")
                continue

            while j < len(self._questions):
                if lines[int(number) - 1] == self._questions[j]:
                    repeat = True
                j += 1
            if repeat == True:
                print("Question already in your survey ! ")
                continue
            self._questions.append(lines[int(number) - 1])
            print("Question number " + str(int(number)) + " added.")
            i += 1
        return 0
    
    def new_response(self):
        response = SurveyResponse(self._id_response)
        self._responses.append(response)
        self._id_response += 1
        return 0
