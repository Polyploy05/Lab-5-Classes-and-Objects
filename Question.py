'''
Names: Jacob Miranda & Daniel Puerto
Date: 2/17/2626
Group: 7
Description: The program should read in a file of state capitals, then quiz the 
user on the capitals of 10 randomly selected states. The user should be given 4 possible 
answers for each question, and the program should keep track of the user's score. The main file 
should loop 10 times, asking a question each time, and then record and display the user's final score at the end.
'''



import random

class Question:

        def __init__ (self,state):
        #Opens the file and creates a dictionary of state-capital pairs
        with open("statecapitals.txt", 'r') as f:
            capitals = {}
            for line in f:
                row = line.rstrip('\n').split(',')
                if row and len(row) >= 2:
                    capitals[row[0]] = row[1]
        #Sets the state to what is provided, then finds the correct capital
        self._state = state
        self._correct_capital = capitals[state]
        self._possible_choices = ["A", "B", "C", "D"]

        #Creates the first answer as the correct capital, then adds random capitals 
        #until there are 4 answers, and shuffles them
        self._answers = [self._correct_capital]
        while len(self._answers) < 4:
            random_capital = random.choice(list(capitals.values()))
            if random_capital not in self._answers:
                self._answers.append(random_capital)
        random.shuffle(self._answers)

        #Combines the possible choices and answers into a dictionary for easy access
        self._selections = {}
        for i in range(len(self._answers)):
            self._selections[self._answers[i]] = self._possible_choices[i]
        
        self._answer = self._selections.get(self._correct_capital)
        





    
    def correct_response(self):
        pass



    def __str__(self):


        pass




