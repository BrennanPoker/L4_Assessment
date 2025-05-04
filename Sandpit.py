import random

# Problem generator
def generate_problem(problem_type):
    """ Generates a problem for user to solve"""
    height = random.randint(1,15)
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

    elif problem_type == "area_triangle":
        area_t = (base * height) / 2
        problem = f"A triangle has a base of {base}mm and a height of {height}mm. What is the area?"
        answer = area_t

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
    question_type = random.choice(["area_square", "perimeter_rectangle", "area_triangle",
                                   "perimeter_square", "area_rectangle", "perimeter_triangle"])
    return generate_problem(question_type)

def generate_problem(problem_type):
    """ Generates a problem for user to solve"""
    if problem_type == "area_square":
        height = random.randint(1, 15)
        width = random.randint(1, 15)
        area = height * width
        problem = f"The height of the square is {height}m and the width is {width}m. What is the area?"
        answer = area

    elif problem_type == "perimeter_rectangle":
        base = random.randint(1, 15)
        height = random.randint(1, 15)
        perimeter = 2 * (base + height)
        problem = f"A rectangle has a base of {base}km and a height of {height}km. What is the perimeter?"
        answer = perimeter

    elif problem_type == "area_triangle":
        base = random.randint(5, 15)
        height_t = random.randint(1, 10)
        area_t = (base * height_t) / 2
        problem = f"A triangle has a base of {base}mm and a height of {height_t}mm. What is the area?"
        answer = area_t

    elif problem_type == "perimeter_square":
        side = random.randint(1, 15)
        solution = side * 4
        problem = f"One side of a square is equal to {side}m. What is the perimeter?"
        answer = solution

    elif problem_type == "area_rectangle":
        width = random.randint(1, 15)
        height_r = random.randint(1, 15)
        area_r = width * height_r
        problem = f"A rectangle has a width of {width}km and a height of {height_r}km. What is the area?"
        answer = area_r

    elif problem_type == "perimeter_triangle":
        side_t = random.randint(1, 15)
        perimeter_t = side_t * 3
        problem = f"One side of an equilateral triangle is {side_t}mm. What is the perimeter?"
        answer = perimeter_t

    else:
        raise ValueError("Invalid problem type")

    return problem, answer


