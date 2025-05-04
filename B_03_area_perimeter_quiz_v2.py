import random


# Functions to generate random questions
def generate_area_square_problem():
    height = random.randint(1, 15)
    width = random.randint(1, 15)
    area = height * width
    problem = f"The height of the square is {height}m and the width is {width}m. What is the area?"
    answer = area
    return problem, answer


def generate_perimeter_rectangle_problem():
    base = random.randint(1, 15)
    height = random.randint(1, 15)
    perimeter = 2 * (base + height)
    problem = f"A rectangle has a base of {base}km and a height of {height}km. What is the perimeter?"
    answer = perimeter
    return problem, answer


def generate_area_triangle_problem():
    base = random.randint(5, 15)
    height_t = random.randint(1, 10)
    area_t = (base * height_t) / 2
    problem = f"A triangle has a base of {base}mm and a height of {height_t}mm. What is the area?"
    answer = area_t
    return problem, answer


def generate_random_question():
    question_type = random.choice([
        'area_square', 'perimeter_rectangle', 'area_triangle'
    ])

    if question_type == 'area_square':
        return generate_area_square_problem()
    elif question_type == 'perimeter_rectangle':
        return generate_perimeter_rectangle_problem()
    elif question_type == 'area_triangle':
        return generate_area_triangle_problem()


# Functions to check user input
def string_checker(question, valid_ans=('yes', 'no')):
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:
        user_response = input(question).lower()
        for item in valid_ans:
            if item == user_response:
                return item
            elif user_response == item[0]:
                return item
        print(error)


def instructions():
    print(''' 
*** Instructions ***

To begin, choose the number of rounds (or press <enter> for
infinite mode).

You will have to solve different area and perimeter problems.
Try to get as many problems correct for a higher final score.

Press <xxx> to end the game at any time.

Good Luck!
    ''')


def int_check(question):
    while True:
        error = "Please enter a number that is more than 0\n"
        response = input(question)

        if response == "":
            return "infinite"
        if response.lower() == "xxx":
            return "xxx"

        try:
            response = int(response)
            if response > 0:
                return response
            else:
                print(error)
        except ValueError:
            print(error)


# Main Routine Starts here

# Initialise game variables
mode = "regular"
rounds_played = 0
game_history = []
all_scores = []

# welcomes user to the game
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

# Game loop starts here
score = 0  # To track score
while rounds_played < num_rounds:
    if mode == "infinite":
        rounds_heading = f"\n🏳️🏴🏳️ Round {rounds_played + 1} (infinite mode) 🏳️🏴🏳️"
    else:
        rounds_heading = f"\n💿💿💿 Round {rounds_played + 1} of {num_rounds}"

    print(rounds_heading)
    print()

    # Generate a random question
    question, correct_answer = generate_random_question()

    # Ask perimeter and area question and get the user's answer
    print(question)
    user_answer = input("Answer: ")

    # Check for quit condition
    if user_answer.lower() == "xxx":
        print("You have exited the quiz.")
        break

    # Check if the user answered correctly
    try:
        if float(user_answer) == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {correct_answer}\n")
    except ValueError:
        print(f"Invalid input. The correct answer was {correct_answer}\n")

    rounds_played += 1

    # If users are in infinite mode, increase the number of rounds
    if mode == "infinite":
        num_rounds += 1
# Game loop ends here

# check users have played at least one round
# before calculating statistics
if rounds_played > 0:
    # Game History / Statistics area

    # Calculate statistics
    all_scores.sort()
    best_score = all_scores[0]
    worst_score = all_scores[-1]
    average_score = sum(all_scores) / len(all_scores)

    # Output the statistics
    print("\n📊📊📊 Statistics 📊📊📊")
    print(f"Best: {best_score} | Worst: {worst_score} | Average: {average_score:.2f} ")
    print()

    # Display the game history on request!
    while True:
        ask_history = string_checker("\nDo you want quiz history? ")

        ask_history = ask_history.lower()

        if ask_history == "yes":
            for item in game_history:
                print(item)
            break

        elif ask_history == "no":
            break

    print("\nThank you for participating in this Quiz")

else:
    print("🐔🐔🐔 Oops - You chickened out! 🐔🐔🐔")
