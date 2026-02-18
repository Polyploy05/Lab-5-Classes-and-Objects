'''
Names: Jacob Miranda & Daniel Puerto
Date: 2/17/2626
Group: 7
Description: A class that creates a question by picking a random state from the provided dictionary and saving it 
alongside it's coresponding capital. It then adds 3 more possible capital choices, shuffles them all, and 
sets each capital to a dictionary list and letter value A-D. Has functions to return all possible choices,
check for the correct choice, and read out a standard correct or incorrect responce. Object-to-string prints
out the whole question with every possible answer
'''

import random

class Question:

    '''Creates a question for use with the quiz code. 
    Attributes: 
    _state (str): The state to be used for the question
    _correct_capital (str): The capital corresponding to the chosen state
    _possible_choices (Str list): All possible inputs A-D
    _selections (Str list): All the capitals that correspond to each possible input. Includes the correct
    capital and 3 incorrect ones. All 4 are unique from one another
    _answer (str): The input corresponding to the correct capital
    '''
    def __init__ (self,states):
        #Sets the state to what is provided, then finds the correct capital
        num = random.randint(0, len(states)-1)

        self._state = list(states.keys())[num]
        self._correct_capital = states.get(self._state)
        self._possible_choices = ["A", "B", "C", "D"]

        #Creates the first answer as the correct capital, then adds random capitals 
        #until there are 4 answers, and shuffles them
        self._answers = [self._correct_capital]
        while len(self._answers) < 4:
            random_capital = random.choice(list(states.values()))
            if random_capital not in self._answers:
                self._answers.append(random_capital)
        random.shuffle(self._answers)

        #Combines the possible choices and answers into a dictionary for easy access
        self._selections = {}
        for i in range(len(self._answers)):
            self._selections[self._answers[i]] = self._possible_choices[i]
        
        self._answer = self._selections.get(self._correct_capital)
        

    def check_correct(self, user_choice):
        #Checks and return whether the user's choice is correct by comparing it to the correct answer
        return user_choice == self._answer

    def possible_choices(self):
        return self._possible_choices

    
    def correct_response(self):
        return f"Correct! The capital of {self._state} is {self._correct_capital}."

    def incorrect_response(self):
        return f"Incorrect. The capital of {self._state} is {self._correct_capital}."


    def __str__(self):
        #Lists the question and all possible answers, with each answer being a new line
        output = f"The capital of {self._state} is: \n"
        for key, value in self._selections.items():
            output += f"{value}. {key}\n"
        return output






