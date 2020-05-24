# Test-Driven Development (TDD)

During this project, I tried to follow the TDD methodology.
It was really difficult to make this methodology possible with this project because of the prompt.

## The prompt
To make the SurveyController possible, I made a prompt with 10 commands. Once those commands created, and the inputs handled, I managed to make my first unit tests. The Survey class was already begun when those tests were made. (See Project Log Document)

## First Unittest file

At this point, I created the first unit test file in this branch : https://github.com/papaiou/SoftwareQualityAssurance-FinalAssesment/pull/7

The only way to test a prompt is to make an  ```echo -e``` in a Command Line Interface (CLI). So I reproduced the entire user experience, separating each input by an ```\n```. So I entirely covered the existant code (with the 4 firsts methods) and tried to create the future unit test for the 5 remaining methods.


## Second unit test wave

We can see those unit tests here : https://github.com/papaiou/SoftwareQualityAssurance-FinalAssesment/pull/11

Unit tests were focused on SurveyResponse class and the statistical methods.

The final goal was to find every possible user experience and handle it in our Unittest program.

## Last problem with unit test?

At the end of the project, a problem occurred with the add_question() method test. I was obliged to split one unit test outside of the unit test file. Indeed, this test changes the database's number of questions and many other tests are based on this value.