from utils import read_file


def update_signal_sum_if_interesting_cycle(signal_sum, cycle, register):
    if (cycle - 20) % 40 == 0:
        return signal_sum + (cycle * register)
    return signal_sum


def problem_10_1():
    input_lines = read_file("./inputs/10_1.txt")

    signal_sum = 0
    cycle = register = 1
    for instruction in input_lines:
        signal_sum = update_signal_sum_if_interesting_cycle(signal_sum, cycle, register)

        if instruction.startswith("noop"):
            cycle += 1

        if instruction.startswith("addx"):
            cycle += 1
            signal_sum = update_signal_sum_if_interesting_cycle(signal_sum, cycle, register)

            cycle += 1
            register += int(instruction.split()[-1])

    return signal_sum


SCREEN_WIDTH = 40


def draw_pixel(cycle, register):
    # Newline if necessary
    if cycle % SCREEN_WIDTH == 0:
        print()

    if abs((cycle - 1) % SCREEN_WIDTH - register) < 2:
        print("#", end="")
    else:
        print(".", end="")


def problem_10_2():
    input_lines = read_file("inputs/10_1.txt")

    cycle = register = 1
    for instruction in input_lines:
        draw_pixel(cycle, register)

        if instruction.startswith("noop"):
            cycle += 1

        if instruction.startswith("addx"):
            cycle += 1
            draw_pixel(cycle, register)

            cycle += 1
            register += int(instruction.split()[-1])

    return


print(f"Problem 10 - 1: {problem_10_1()}")
print(f"Problem 10 - 2: {problem_10_2()}")
