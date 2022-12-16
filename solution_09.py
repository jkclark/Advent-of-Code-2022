"""
Positions are stored as (x, y) = (horizontal, vertical)
Starting point for H and T (and S) is (0, 0)
"""
from utils import read_file


def get_new_position(original_position, direction):
    if direction == "U":
        return (original_position[0], original_position[1] + 1)
    if direction == "D":
        return (original_position[0], original_position[1] - 1)
    if direction == "L":
        return (original_position[0] - 1, original_position[1])
    if direction == "R":
        return (original_position[0] + 1, original_position[1])


def problem_09_1():
    input_lines = read_file("inputs/09_1.txt")

    head = tail = (0, 0)
    tail_positions = set()
    tail_positions.add(tail)
    for line in input_lines:
        direction, steps = line.split()
        for step in range(int(steps)):
            # Get new head position
            new_head = get_new_position(head, direction)

            # If this is too far from tail, move tail
            if abs(new_head[0] - tail[0]) > 1 or abs(new_head[1] - tail[1]) > 1:
                tail = head
                tail_positions.add(tail)

            head = new_head

    return len(tail_positions)


def problem_09_2():
    input_lines = read_file("inputs/09_1.txt")

    raise NotImplementedError


print(f"Problem 09 - 1: {problem_09_1()}")
print(f"Problem 09 - 2: {problem_09_2()}")
