'''
Names: Jacob Miranda & Daniel Puerto
Date: 2/17/2626
Group: 7
Description: The program should read in a file of state capitals, then quiz the 
user on the capitals of 10 randomly selected states. The user should be given 4 possible 
answers for each question, and the program should keep track of the user's score. The main file 
should loop 10 times, asking a question each time, and then record and display the user's final score at the end.
'''



import Question

def read_file_to_dictionary(statecapitals):
    #Reads states,capital pairs from the file into a dictionary and returns it.
    states = {}
    with open("statecapitals.txt", 'r') as f:
        for line in f:
            row = line.rstrip('\n').split(',')
            if row and len(row) >= 2:
                states[row[0]] = row[1]
    return states


def get_user_choice(valid_options):
    #Repeatedly prompts and checks until the user enters a valid choice (A–D).
    valid = False
  while not valid:
    val = input(prompt).upper()
    if val == "A" or val == "B" or val == "C" or val == "D":
      return True
    else:
        print(f"Invalid input - enter {valid_options[0]}–{valid_options[-1]}.")


def ask_questions(number, states):
    #Creates a Question, pompots it, checks whether the answer is corect and returns it as a 1 (correct) or 0 (incorrect).
    print(f"{number}.", end="")

    q = Question.Question(states)
    print(q)

    user_choice = get_user_choice(q.possible_choices())

    if q.check_correct(user_choice):
        print(q.correct_response())
        return 1
    else:
        print(q.incorrect_response())
        return 0 
    

def main():
    # Displays the quiz header
    print("Welcome to the State Capitals Quiz")

    #Reads the state-capital pairs from the file into a dictionary
    states = read_file_to_dictionary("statecapitals")

    #Keeps track of the user's total score
    score = 0

    #Asks the 10 questions, 1-10
    for i in range(1,11):
        print()
        score += ask_questions(i, states)

    #After all the questions are complete, shows the final score
    print("\nQuiz complete")
    print(f"You scored {score} out of 10.")


if __name__ == "__main__":
    main()









