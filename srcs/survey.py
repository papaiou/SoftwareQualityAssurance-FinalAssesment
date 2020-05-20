# !/usr/bin/env python
# -*- coding: utf-8 -*-

from srcs.survey_response import SurveyResponse

class Survey:
    def __init__(self, id, namelist):
        self._responses = []
        self._id = id
        self._id_response = 0
        self.new_survey()
        self._name = ""
        while not self._name:
            self._name = input("What is the name of your new Survey? : ")
            if self.check_name(namelist) == 0:
                print("Name already used for another Survey !")
                self._name = ""

    def check_name(self, namelist):
        for name in namelist:
            if name == self._name:
                return 0
        return 1

    def new_survey(self):
        print("currently creating a new survey.")
        return 0
    
    def new_response(self):
        response = SurveyResponse(self._id_response)
        self._responses.append(response)
        self._id_response += 1
        return 0
