def int_check(question):
    while True:
        error = "\nPlease enter a number that is more than 0"

        # check for infinite mode when input is empty (user presses enter)
        response = input(question)

        if response == "":  # If no input, return "infinite"
            return "infinite"

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

print("⬆️⬆️⬆️ Welcome to the Higher Lower Game ⬇️⬇️⬇️")
print()

# Ask user for number of rounds / infinite mode
num_rounds = int_check("Rounds <enter for infinite>")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Get game parameters


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
    user_choice = input("Choose: ")

    # if user choice is the exit code, break the loop
    if user_choice == "xxx":
        break

    rounds_played += 1

    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1
