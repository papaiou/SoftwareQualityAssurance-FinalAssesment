# SurveyController class

This class is called by the main function and manages the prompt. It is the core of the monitor.

Here are the datas we can find in this class :

`surveys` : [Surveys] : Array of all Surveys created.

`servey_names` : [String] : Array of the name of each Survey created.

`id_counter` : Int : Actual number of Surveys in the monitor. The next Survey will have this value in the id variable.


Here are all the methods we can find in this class :

`__init__` : Constructor of the class. Starts the prompt

`print_help` : Print help panel for different usages.

`new_survey` : Method who creates a Survey class.

`exit_input` : Method who exits the prompt and the program.

`add_question` : Method who permanently adds a question to our fake database.

`get_survey` : Method who retrieves all information available about a Survey.

`survey_list` : Method who list and print all Surveys created.

`survey_stats` : Method who retrieves all statistics about a Survey and call the survey_stats() method of the Survey class for the display.

`question_stats` : Method who retrieves all statistics about a question Survey and call the survey_question_stats() method of the Survey class for the display.

`new_survey_response` : Method who directly calls the new_survey_response() of the Survey class concerned.

`get_survey_response` : Method who retrieves all information available about a SurveyReponse.

`input_start` : Method called recursively. That's how the prompt work. Main input will be compared to all possibilities and trigger the right method thanks to the input.