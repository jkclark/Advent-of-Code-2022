from collections import deque

from utils import read_file


def get_stack_and_move_inputs(file_input):
    # Strategy here is to parse through the entire input file once,
    # separating the crate-describing lines from the move-describing lines.
    # Then, we'll parse those two pieces of input separately.
    FIRST_NON_CRATE_LINE_PREFIX = " 1 "
    crate_input = []
    move_input = []
    crate_mode = True
    for line in file_input:
        if line == "\n":  # Skip the emtpy line between crates & moves
            continue

        if crate_mode:
            if line.startswith(FIRST_NON_CRATE_LINE_PREFIX):
                crate_mode = False
                continue
                
            crate_input.append(line)
        else:
            move_input.append(line)

    return crate_input, move_input


def create_stacks(crate_input):
    NUM_STACKS = len(crate_input[0]) // 4
    stacks = [deque() for _ in range(NUM_STACKS)]
    for crate_line in crate_input:
        stack_index = 0
        for stack_index in range(NUM_STACKS):
            _, letter, _, _ = crate_line[stack_index * 4: stack_index * 4 + 4]
            if letter != " ":
                stacks[stack_index].append(letter)

    return stacks


def move_crates_from_stack_to_stack(num_crates, from_stack, to_stack):
    """NOTE: This function modifies its input arguments."""
    for _ in range(num_crates):
        to_stack.appendleft(from_stack.popleft())


def move_crates_from_stack_to_stack_keep_order(num_crates, from_stack, to_stack):
    """NOTE: This function modifies its input arguments.

    This function works by using a temporary stack, adding crates to that stack,
    then popping and pushing to the destination stack, thereby maintaining the
    original order.
    """
    # Move from starting stack to temp stack
    temp_stack = deque()
    for _ in range(num_crates):
        temp_stack.appendleft(from_stack.popleft())

    # Move from temp stack to destination stack
    while temp_stack:
        to_stack.appendleft(temp_stack.popleft())


def move_crates(stacks, moves, keep_order=False):
    """NOTE: This function modifies its input argument."""
    for move in moves:
        _, num_crates, _, from_stack, _, to_stack = move.split()
        if keep_order:
            move_crates_from_stack_to_stack_keep_order(int(num_crates), stacks[int(from_stack) - 1], stacks[int(to_stack) - 1])
        else:     
            move_crates_from_stack_to_stack(int(num_crates), stacks[int(from_stack) - 1], stacks[int(to_stack) - 1])


def problem_05_1():
    # Parse input
    crates_and_moves = read_file("inputs/05_1.txt")

    crate_input, move_input = get_stack_and_move_inputs(crates_and_moves)

    stacks = create_stacks(crate_input)

    # Manipulate crate stacks based on move inputs
    move_crates(stacks, move_input)

    # Print answer
    return "".join([stack[0] for stack in stacks])


def problem_05_2():
    crates_and_moves = read_file("inputs/05_1.txt")

    crate_input, move_input = get_stack_and_move_inputs(crates_and_moves)

    stacks = create_stacks(crate_input)

    move_crates(stacks, move_input, keep_order=True)

    return "".join([stack[0] for stack in stacks])

    
print(f"Problem 05 - 1: {problem_05_1()}")
print(f"Problem 05 - 2: {problem_05_2()}")