import random

def generate_random_integer(min_value, max_value):
    """
    To generate a random integer between min_value and max_value.

    Parameters of the function :
    1. min_value (int): The minimum value for the random integer.
    2. max_value (int): The maximum value for the random integer.

    Returns:
    randint - A randomly generated integer. (int)
    """
    return random.randint(min_value, max_value)

def generate_random_operator():
    """
    To generate a random arithmetic operator: '+', '-', or '*'.

    Returns:
    choice - A randomly selected arithmetic operator. (str)
    """
    return random.choice(['+', '-', '*'])

def perform_operation(num1, num2, operator):
    """
    Perform an arithmetic operation based on the given numbers and operator.
    Return a tuple containing the problem and the correct answer.

    Parameters:
    1. num1 (int): The first operand.
    2. num2 (int): The second operand.
    3. operator (str): The arithmetic operator ('+', '-', or '*').

    Returns:
    tuple: A tuple containing the arithmetic problem as a string and the correct answer.
    """
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    else:
        result = num1 * num2

    problem = f"{num1} {operator} {num2}"
    return problem, result

def get_user_input():
    """
    To get user input for the answer and handle potential input errors.

    Returns:
    int: User's answer as an integer.

    Error Handling using try and except.
    """
    while True:
        try:
            user_input = input("Your answer: ")
            user_answer = int(user_input)
            return user_answer
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def math_quiz():
    """
    In order to conduct a math quiz game, we are presenting the user with random arithmetic problems.

    It prints the questions, accepts user input for answers, and provides feedback on correctness. Finally it
    displays the final score at the end.
    """
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    # Looping through the number of inputs
    for _ in range(total_questions):
        # Generate random numbers and operator for the current question
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)
        operator = generate_random_operator()

        # Perform the operation and get the problem and correct answer
        problem, answer = perform_operation(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        # Get user input for the answer with error handling
        user_answer = get_user_input()

        # Check if the user's answer is correct
        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    # Display the final score
    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
