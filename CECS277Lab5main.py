'''
Names:
Date:
Group:
Description:
'''



import Question

def read_file_to_dictionary(statecapitals):
    
    states = {}
    with open(statecapitals, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                state,capital = line.split(",")
                state[state] = capital
    return states


def get_user_choice(valid_options):
    
    choice = input("Enter choice: "). upper()

    while choice not in valid_options:
        print(f"Invalid input. Enter {valid_options[0]} - {valid_options[-1]}.")
        choice = input("Enter choice: ").upper()

    return choice


def ask_questions(number, states):

    print(f"{number}.", end="")

    q = Question(states)
    print(q)

    user_choice = get_user_choice(q.possible_choices)

    if q.check_correct(user_choice):
        print(q.correct_response())
        return 1
    else:
        print(q.incorrect_response())
        return 0 
    

def main():
    print("Welcome to the State Capitals Quiz")

    states = read_file_to_dictionary("statecapitals.txt")

    score = 0
    for i in range(1,11):
        print()
        score += ask_questions(i, states)


    print("\nQuiz complete")
    print(f"You scored {score} out of 10.")


if __name__ == "__main__":

    main()
