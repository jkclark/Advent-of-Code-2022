from utils import read_file


def find_line_group_sums(lines):
    current_sum = 0
    for line in lines:
        if line == "\n":
            yield current_sum
            current_sum = 0

        else:
            current_sum += int(line)


def problem_01_1():
    calories = read_file("inputs/01_1.txt")

    max_calories = 0
    for calorie_sum in find_line_group_sums(calories):
        if calorie_sum > max_calories:
            max_calories = calorie_sum

    return max_calories


def problem_01_2():
    calories = read_file("inputs/01_1.txt")

    # First, space-inefficient approach
    return sum(sorted([
        single_food_calories
        for single_food_calories in find_line_group_sums(calories)
    ], reverse=True)[:3])


print(f"Problem 01 - 1: {problem_01_1()}")
print(f"Problem 01 - 2: {problem_01_2()}")