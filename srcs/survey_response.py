# !/usr/bin/env python
# -*- coding: utf-8 -*-

class SurveyResponse:
    def __init__(self, id):
        self._id = id
        self.new_survey_response()

    def new_survey_response(self):
        print("new survey response created")
        return 0