import random


# Problem generator
def generate_problem(problem_type):
    """ Generates a problem for user to solve"""
    height = random.randint(1, 15)
    width = random.randint(1, 15)
    base = random.randint(5, 15)
    side = random.randint(1, 15)

    if problem_type == "area_square":
        area = height * width
        problem = f"The height of the square is {height}m and the width is {width}m. What is the area?"
        answer = area

    elif problem_type == "perimeter_rectangle":
        perimeter = 2 * (base + height)
        problem = f"A rectangle has a base of {base}km and a height of {height}km. What is the perimeter?"
        answer = perimeter

    elif problem_type == "perimeter_square":
        solution = side * 4
        problem = f"One side of a square is equal to {side}m. What is the perimeter?"
        answer = solution

    elif problem_type == "area_rectangle":
        area_r = width * height
        problem = f"A rectangle has a width of {width}km and a height of {height}km. What is the area?"
        answer = area_r

    elif problem_type == "perimeter_triangle":
        perimeter_t = side * 3
        problem = f"One side of an equilateral triangle is {side}mm. What is the perimeter?"
        answer = perimeter_t

    else:
        raise ValueError("Invalid problem type")

    return problem, answer


# Prints the random problem question
def generate_random_question():
    """ Selects a random problem from generate_problem """
    question_type = random.choice(["area_square", "perimeter_rectangle", "perimeter_square",
                                   "area_rectangle", "perimeter_triangle"])
    return generate_problem(question_type)


# Functions to check user input
def string_checker(question, valid_ans=('yes', 'no')):
    """ Makes sure user selects either yes or no """
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:
        user_response = input(question).lower()
        for item in valid_ans:
            if item == user_response:
                return item
            elif user_response == item[0]:
                return item
        print(error)


# Prints instructions
def instructions():
    """ Prints instructions """
    print(''' 
*** Instructions ***

To begin, choose the number of rounds (or press <enter> for
infinite mode).

You will have to solve different area and perimeter problems.
Try to get as many problems correct for a higher final score.

Press <xxx> to end the quiz at any time.

Good Luck!
    ''')


# Makes sure user enters a valid number or xxx to quit
def int_check(question):
    """Makes sure user enters a valid number or 'xxx' to quit."""
    while True:
        response = input(question).lower()

        if response == "xxx":
            return response
        if response == "":
            return "infinite"
        if response == "0":
            print("❌ Enter a number greater than 0 ❌")
            continue

        try:
            return int(response)
        except ValueError:
            print("❌ Invalid input! Please enter a valid number. ❌")


# Main Routine Starts here

# Initialise quiz variables
mode = "regular"
rounds_played = 0
quiz_history = []

# welcomes user to the quiz
print("☐▭🛆 Welcome to Area and Perimeter Quiz 🛆▭☐")
print()

# Instructions
want_instructions = string_checker("Do you want to read the instructions? ")

if want_instructions == "yes":
    instructions()

# Ask user for number of rounds / infinite mode
num_rounds = int_check("Rounds <enter for infinite>")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Quiz loop starts here
score = 0
while rounds_played < num_rounds:
    if mode == "infinite":
        rounds_heading = f"\n🏳️🏴🏳️ Round {rounds_played + 1} (infinite mode) 🏳️🏴🏳️"
    else:
        rounds_heading = f"\n💿💿💿 Round {rounds_played + 1} of {num_rounds} 💿💿💿"

    print(rounds_heading)
    print()

    # Generate a random question
    question, correct_answer = generate_random_question()

    # Ask perimeter and area question and get the user's answer
    print(question)
    user_answer = int_check("Answer: ")

    # Check for quit condition
    if user_answer == "xxx":
        print("You have exited the quiz.")
        break

    # Check if the user answered correctly
    if user_answer == correct_answer:
        print("Correct!\n")
        score += 1
    else:
        print(f"Incorrect. The correct answer was {correct_answer}\n")

    rounds_played += 1

    # If users are in infinite mode, increase the number of rounds
    if mode == "infinite":
        num_rounds += 1

    # Gives user feedback
    if float(user_answer) == correct_answer:
        feedback = "Correct!"
    else:
        feedback = "Wrong!"

    # Add round result to quiz history
    history_feedback = f"Round {rounds_played}: {feedback} - {question} | Your Answer: {user_answer} / " \
                       f"Correct answer: {correct_answer}"
    quiz_history.append(history_feedback)

# Quiz loop ends here


# Quiz History / Statistics area
if rounds_played > 0:

    # Output Quiz Statistics
    print("\n📊📊📊 RESULTS 📊📊📊")
    if score == 0:
        print("Oh no! You got None Right... Better Luck Next Time")

    if rounds_played == score:
        print("You got every answer correct! Congratulations!")
        print(f"Your score is {score} out of {rounds_played}")

    else:
        print(f"👍 Your score is {score} out of {rounds_played} 👎")

    # Asks if they want quiz history
    while True:
        ask_history = string_checker("\nDo you want quiz history? ")

        ask_history = ask_history.lower()

        if ask_history == "yes":
            for item in quiz_history:
                print(item)
            break

        elif ask_history == "no":
            break

    print("\nThank you for playing area and perimeter quiz!")
