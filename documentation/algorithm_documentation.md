# Algorithm documentation

This algorithm was made with 3 classes.

## SurveyController Class

This class represents the prompt of the project. It handles 10 commands and different ways to understand a command. You can see available commands [here](./SurveyController_documentation.md).

This class is the only thing called by the main function and it calls the two other classes of the project.

## Survey class

This class manages each survey and keep all information that a survey and its responses need. Each survey is unique and stored in the SurveyController class. You can find more information about this class [here](./Survey_documentation.md).

## SurveyResponse class

This class is created when we want to create a new survey response. It will store each answer in an array inside of the class. Each SurveyRepsonse is appended to an array in the Survey class. You can see more information about this class [here](SurveyResponse_documentation.md)