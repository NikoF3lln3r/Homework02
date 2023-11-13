import random


def random_integer(min, max):
    """Return a random number between min and max

    Parameters:
    min (int): minimal value
    max (int): maximal value

    Returns:
    int: Returning value
   """
    return random.randint(min, max)


def random_math_operator():
    """Return a random choice of mathematical operation (+, -, *)

    Parameters:
        None

    Returns:
        char: single character representing the mathematical operation

   """
    return random.choice(['+', '-', '*'])


def math_operation(number_1, number_2, operator):
    """performs the mathematical operation given 2 numbers and one operation

    Parameters:
        number_1 (int): first number
        number_2 (int): second number
        operator (char): operation

    Returns:
       solution (double): Solution of the mathematical operation
       operation_string (string): representing the mathematical operation
   """

    # differentiate the three cases which are +, - and *
    operation_string = f"{number_1} {operator} {number_2}"
    if operator == '-':
        solution = number_1 - number_2
    elif operator == '+':
        solution = number_1 + number_2
    else:
        solution = number_1 * number_2
    return operation_string, solution

def math_quiz_game(number_questions = 3):
    """performs the mathematical operation given 2 numbers and one operation

    Parameters:
        NUN_QUESTIONS (int): default = 3, shows the number of questions until the game ends

    Returns:

   """
    number_questions = number_questions
    score = 0
    max_score = number_questions

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    # iterate over the number of iterations
    for _ in range(number_questions):
        is_answer_good = False
        # getting all needed variables for mathematical operation
        number_1 = random_integer(1, 10)
        number_2 = random_integer(1, 5)
        operator = random_math_operator()

        # solve the mathematical problem and getting the result
        problem, result = math_operation(number_1, number_2, operator)
        print(f"\nQuestion: {problem}")

        # as long as the user does not give a valid input, he is asked for an input
        while not is_answer_good:
            try:
                useranswer = int(input("Your answer: "))
            except ValueError:
                print("Add valid number")
                continue
            is_answer_good = True

        # comparing the result of the function with the input of the user, if correct -> increase score
        if useranswer == result:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {result}.")

    print(f"\nGame over! Your score is: {score}/{max_score}")

if __name__ == "__main__":
    math_quiz_game()
