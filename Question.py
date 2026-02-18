'''
Names: Jacob Miranda & Daniel Puerto
Date: 2/17/2626
Group: 7
Description: 
'''
import random


class Question:


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
        return user_choice == self._answer

    def possible_choices(self):
        return self._possible_choices

    
    def correct_response(self):
        return f"Correct! The capital of {self._state} is {self._correct_capital}."

    def incorrect_response(self):
        return f"Incorrect. The capital of {self._state} is {self._correct_capital}."


    def __str__(self):
        output = f"The capital of {self._state} is: \n"
        for key, value in self._selections.items():
            output += f"{value}. {key}\n"
        return output








