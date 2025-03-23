# Functions go here
# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans=('yes', 'no')):
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()


# Displays instructions
def instructions():
    print(''' 
*** Instructions ***

To begin, choose the number of rounds (or press <enter> for
infinite mode).

You will have to solve different area and perimeter problems.
Try get as much problems correct for a higher final score.

Press <xxx> to end game at anytime.

Good Luck!
    ''')


# Checks user enters an integer more than / equal to 0
def int_check(question):
    while True:
        error = "Please enter a number that is more than 0\n"

        # check for infinite mode when input is empty (user presses enter)
        response = input(question)

        if response == "":
            return "infinite"
        if response.lower() == "xxx":
            return "xxx"

        try:
            response = int(response)

            # check that the number is more than zero
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

shape_list = ["Square", "Rectangle", "Triangle"]
game_history = []

# welcomes user to the game
print("☐▭🛆 Welcome to Area and Perimeter Game 🛆▭☐")
print()

# Instructions

want_instructions = string_checker("Do you want to read the instructions? ")

# if the user wants instructions then print instructions
if want_instructions == "yes":
    instructions()

# Ask user for number of rounds / infinite mode
num_rounds = int_check("Rounds <enter for infinite>")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings
    if mode == "infinite":
        rounds_heading = f"\n🏳️🏴🏳️ Round {rounds_played + 1} (infinite mode) 🏳️🏴🏳️"
    else:
        rounds_heading = f"\n💿💿💿 Round {rounds_played + 1} of {num_rounds}"

    print(rounds_heading)
    print()

    # get user choice
    user_choice = int_check("Answer: ")

    # if user choice is the exit code, break the loop
    if user_choice == "xxx":
        break

    rounds_played += 1

    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1

# Statistics and Game History
