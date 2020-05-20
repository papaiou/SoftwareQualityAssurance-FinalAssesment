# !/usr/bin/env python
# -*- coding: utf-8 -*-

from srcs.survey_response import SurveyResponse

class Survey:
    def __init__(self, id):
        self._responses = []
        self._id = id
        self._id_response = 0
        self.new_survey()

    def new_survey(self):
        print("currently creating a new survey.")
        return 0
    
    def new_response(self):
        response = SurveyResponse(self._id_response)
        self._responses.append(response)
        self._id_response += 1
        return 0
