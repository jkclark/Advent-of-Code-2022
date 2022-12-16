from utils import read_file


def problem_06_1():
    buffer = read_file("inputs/06_1.txt")[0]  # The buffer is the first (and only) line in the file
    START_SIGNAL_SIZE = 14  # 4 for the first half of the problem
    index = 0
    while index < len(buffer):
        if len(set(buffer[index: index + START_SIGNAL_SIZE])) == START_SIGNAL_SIZE:
            return index + START_SIGNAL_SIZE
        index += 1

    return -1

def problem_06_2():
    # The solution the second half of the problem just consisted of
    # changing START_SIGNAL_SIZE from 4 to 14
    pass


print(f"Problem 06 - 1: {problem_06_1()}")
print(f"Problem 06 - 2: {problem_06_2()}")