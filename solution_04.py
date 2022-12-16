from utils import read_file


def determine_section_enclosing(section_1, section_2):
    """Return True if one section completely contains the other, False otherwise."""
    first_encloses_second = section_1[0] <= section_2[0] and section_1[1] >= section_2[1]
    second_encloses_first = section_2[0] <= section_1[0] and section_2[1] >= section_1[1]
    return first_encloses_second or second_encloses_first


def problem_04_1():
    pairs = read_file("inputs/04_1.txt")

    overlap_count = 0
    for pair in pairs:
        section_1, section_2 = pair.split(",")
        overlap_count += determine_section_enclosing(
            [int(id_num) for id_num in section_1.split("-")],
            [int(id_num) for id_num in section_2.split("-")],
        )

    return overlap_count


def determine_section_overlap(section_1, section_2):
    """Return True if the two sections share at least one number, False otherwise."""
    triplets = [
        (section_1[0], section_2[0], section_1[1]),
        (section_1[0], section_2[1], section_1[1]),
        (section_2[0], section_1[0], section_2[1]),
        (section_2[0], section_1[1], section_2[1]),
    ]

    for bottom, middle, top in triplets:
        if bottom <= middle <= top:
            return True
    return False


def problem_04_2():
    pairs = read_file("inputs/04_1.txt")

    overlap_count = 0
    for pair in pairs:
        section_1, section_2 = pair.split(",")
        overlap_count += determine_section_overlap(
            [int(id_num) for id_num in section_1.split("-")],
            [int(id_num) for id_num in section_2.split("-")],
        )

    return overlap_count


print(f"Problem 04 - 1: {problem_04_1()}")
print(f"Problem 04 - 2: {problem_04_2()}")