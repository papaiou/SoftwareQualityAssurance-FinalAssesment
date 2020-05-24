# !/usr/bin/env python
# -*- coding: utf-8 -*-

class SurveyResponse:
    def __init__(self, id, name, questions):
        self._id = id
        self._name = name
        self._responses = []
        self.new_survey_response(questions)

    def new_survey_response(self, questions):
        for question in questions:
            response = 0
            print(question)
            print("1 : Not at all !")
            print("2 : Not really...")
            print("3 : Maybe...")
            print("4 : Probably...")
            print("5 : YES !")
            while response == 0:
                number = input("What is your answer ? : ")
                if not number.isdigit() or int(number) < 1 or int(number) > 5:
                    print("Please enter a number between 1 and 5.")
                    continue
                response = int(number)
            self._responses.append(response)
        return 0