# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import statistics
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
        response_name = ""
        while not response_name:
            response_name = input("What is the name of your new Survey response? : ")
            for response in self._responses:
                if response._name == response_name:
                    print("Name already used for another Survey response!")
                    response_name = ""
        response = SurveyResponse(self._id_response, response_name, self._questions)
        self._responses.append(response)
        self._id_response += 1
        return 0

    def get_response(self):
        if self._id_response == 0:
            print("No repsonses have been created for this survey !")
            return 0
        print("Here are all reponses to this survey : ")
        for response in self._responses:
            print(str(response._id + 1) + " : " + response._name)
        choice = 0
        while choice == 0:
            number = input("Which answer do you want to see ? : ")
            if not number.isdigit() or int(number) < 1 or int(number) > len(self._responses):
                print("Please enter a number between 1 and " + str(len(self._responses)) + ".")
                continue
            choice = int(number)
        choice -= 1
        print("Here are all informations about this survey response :")
        print("Name : " + self._responses[choice]._name)
        print("ID : " + str(self._responses[choice]._id))
        print("Answers (where 1 = \"Not at all !\" // 2 = \"Not really...\" // 3 = \"Maybe...\" // 4 = \"Probably...\" // 5 = \"YES !\") : ")
        i = 0
        while i < self._nb_questions:
            print(str(i + 1) + " : " + self._questions[i] + " --> " + str(self._responses[choice]._responses[i]))
            i += 1
        return 0

    def display_stats(self):
        datas = []
        for response in self._responses:
            for answer in response._responses:
                datas.append(int(answer))
        average = statistics.mean(datas)
        std_dev = statistics.stdev(datas)
        min_value = min(datas)
        max_value = max(datas)
        print("Here are all statistics about this survey :")
        print("Survey name : " + self._name)
        print("Survey ID : " + str(self._id))
        print("Minimum value : " + str(min_value))
        print("Maximum value : " + str(max_value))
        print("Average value : " + str(average))
        print("Standard deviation value : " + str(std_dev))
        return 0

    def display_question_stats(self, i):
        datas = []
        for response in self._responses:   
            datas.append(int(response._responses[i]))
        average = statistics.mean(datas)
        std_dev = statistics.stdev(datas)
        min_value = min(datas)
        max_value = max(datas)
        print("Here are all statistics about this survey :")
        print("Survey name : " + self._name)
        print("Survey ID : " + str(self._id))
        print("Question number : " + str(i))
        print("Minimum value : " + str(min_value))
        print("Maximum value : " + str(max_value))
        print("Average value : " + str(average))
        print("Standard deviation value : " + str(std_dev))
        return 0