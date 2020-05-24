# SurveyResponse documentation

This class is called by the Survey class and gives to this class the possibility to stock responses for its survey.

Here are the datas we can find in this class :

`Id` : Int : Id of the Survey response. (unique)

`Name` : String : Name of the Survey response. (unique)

`Responses` : [Int] : Array containing each answer of the Survey.


Here are all the methods we can find in this class :

`__init__` : Constructor of the class, needs the id, the name and the question that will be asked for the Survey.

`new_survey_response` : Create and build the response of the Survey.