# Survey documentation

This class is called by the SurveyController class and gives to this class the possibility to create different surveys for our monitor.

Here are the datas we can find in this class :

`Id` : Int : Id of the Survey for the SurveyController. (unique)

`Name` : String : Name of the Survey for the SurveyController. (unique)

`Responses` : [SurveyResponse] : Array containing each SurveyResponse of the Survey.

`Nb_questions` : Int : Number of questions in the Survey.

`Id_response` : Int : Actual number of responses to the survey. The next SurveyResponse of this Survey will have this value in the id variable.

`Questions` : [String] : Array of the questions of the Survey


Here are all the methods we can find in this class :

`__init__` : Constructor of the class, needs the id and the name list of the others surveys. This method will trigger the new_survey() method

`new_survey` : Create and build the new Survey.

`check_name` : Method who checks if the name of the survey is not already given to another one.

`new_response` : Method who calls the new_survey_reponse of the SurveyResponse class. This method will retrieve every data it needs in the actual class.

`get_response` : Method who retrieves all information available about a Survey.

`display_stats` : Method who retrieves all statistics available about a Survey.

`display_question_stats` : Method who retrieve all statistics available about a question of a Survey.
