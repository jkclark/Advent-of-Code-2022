import string

from utils import read_file


NUM_LOWERCASE_LETTERS = 26
PRIORITY_STARTING_NUMBER = 1

priorities = {
    **{
        letter: priority + PRIORITY_STARTING_NUMBER
        for priority, letter in enumerate(string.ascii_lowercase)
    },
    **{
        letter: priority + PRIORITY_STARTING_NUMBER + NUM_LOWERCASE_LETTERS
        for priority, letter in enumerate(string.ascii_uppercase)
    },
}


def get_letter_priority(letter):
    return priorities[letter]


def get_common_elements(group_1, group_2):
    return set(group_1).intersection(set(group_2))


def problem_03_1():
    rucksacks = read_file("inputs/03_1.txt")
    return sum(
        get_letter_priority(get_common_elements(
            rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]
        ).pop())  # This set guaranteed to have only 1 item
        for rucksack in rucksacks
    )


def problem_03_2():
    # Clean input
    rucksacks = read_file("inputs/03_1.txt")
    rucksacks = [rucksack.strip() for rucksack in rucksacks]  # Remove trailing newlines
    
    GROUP_SIZE = 3
    curr_rucksack_index = total_priority = 0
    for rucksack_index in range(0, len(rucksacks), GROUP_SIZE):
        r1, r2, r3 = rucksacks[rucksack_index: rucksack_index + GROUP_SIZE]
        common_elements = get_common_elements(r1, r2)
        common_elements = get_common_elements(common_elements, r3)

        # This set guaranteed to have only 1 item
        total_priority += get_letter_priority(common_elements.pop())
        
        curr_rucksack_index += GROUP_SIZE

    return total_priority

print(f"Problem 03 - 1: {problem_03_1()}")
print(f"Problem 03 - 2: {problem_03_2()}")