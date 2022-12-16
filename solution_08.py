from utils import read_file


def convert_input_to_grid(input_lines):
    grid = []
    for line in input_lines:
        row = []
        for digit in line[:-1]:  # Stop before newline character
            row.append(int(digit))
            
        grid.append(row)

    return grid


def find_highest_so_far_for_grid(input_grid):
    """Describing this function in one line is hard.

    The output for this function is an grid which is the same size as the input grid.
    Instead of one number at each point in the grid, the output will contain a 4-ple.
    The 4-ple will indicate the highest number in any direction from the current index,
    exclusive. That is to say, the 4-ple will contain the highest number to the left of
    this index, above this index, to the right of this index, and below this index.
    """
    # Create output grid
    output = []
    for _ in input_grid:
        output.append([[] for _ in range(len(input_grid[0]))])

    # NOTE: I think this might have been cleaner by simply specifying the direction
    #       that we'd iterate the row/col indices and then looping over those pairs.
    #       Instead, we have a bunch of code that is repeated. If I were working on this
    #       for a serious project, I'd refactor this and see how much the code was improved.

    # Iterate from left to right for each row
    for row_index, row in enumerate(input_grid):
        highest_so_far = -1
        for col_index, col in enumerate(row):
            # Set highest so far in output
            output[row_index][col_index].append(highest_so_far)

            # Update highest so far
            highest_so_far = max(col, highest_so_far)

    # Iterate from right to left for each row
    for row_index, row in enumerate(input_grid):
        highest_so_far = -1
        for col_index, col in enumerate(reversed(row)):
            # Set highest so far in output
            # NOTE: In hindsight, I think this might have been simpler by just
            #       iterating through the indices in the order we wanted,
            #       not by trying to be fancy and enumerating.
            output[row_index][len(row) - col_index - 1].append(highest_so_far)

            # Update highest so far
            highest_so_far = max(col, highest_so_far)

    # Iterate from top to bottom for each column
    for col_index in range(len(input_grid[0])):
        highest_so_far = -1
        for row_index in range(len(input_grid)):
            # Set highest so far in output
            output[row_index][col_index].append(highest_so_far)

            # Update highest so far
            highest_so_far = max(input_grid[row_index][col_index], highest_so_far)

    # Iterate from bottom to top for each column
    for col_index in range(len(input_grid[0])):
        highest_so_far = -1
        for row_index in range(len(input_grid) - 1, -1, -1):
            # Set highest so far in output
            output[row_index][col_index].append(highest_so_far)

            # Update highest so far
            highest_so_far = max(input_grid[row_index][col_index], highest_so_far)

    return output


def count_visible_trees(tree_heights, tallest_surrounding_trees):
    visible_trees = 0
    for row_index in range(len(tree_heights)):
        for col_index in range(len(tree_heights[0])):
            for tallest_in_direction in tallest_surrounding_trees[row_index][col_index]:
                if tree_heights[row_index][col_index] > tallest_in_direction:
                    visible_trees += 1
                    break

    return visible_trees


def problem_08_1():
    tree_height_input = read_file("inputs/08_1.txt")

    # Convert input to usable 2D array of digits
    tree_height_grid = convert_input_to_grid(tree_height_input)

    # Find the tallest tree in all 4 directions for each location
    highest_so_far_grid = find_highest_so_far_for_grid(tree_height_grid)

    # Count the number of trees that are taller than every tree in 
    return count_visible_trees(tree_height_grid, highest_so_far_grid)


# NOTE: Pretty hideous approach by copying and pasting very similar code four times.
#       Could definitely be cleaned up. Also, there must be a faster way than to just
#       iterate through the grid in 4 directions for every tree, but I couldn't figure
#       one out in an hour or so of cumulative thinking, so I figured I'd just implement
#       a simple brute-force strategy and move on.
def find_visible_trees_left(tree_grid, row_index, col_index):
    tree_height = tree_grid[row_index][col_index]
    visible_trees = 0
    for next_col in range(col_index - 1, -1, -1):
        visible_trees += 1
        if tree_grid[row_index][next_col] >= tree_height:
            break

    return visible_trees


def find_visible_trees_right(tree_grid, row_index, col_index):
    tree_height = tree_grid[row_index][col_index]
    visible_trees = 0
    for next_col in range(col_index + 1, len(tree_grid[row_index])):
        visible_trees += 1
        if tree_grid[row_index][next_col] >= tree_height:
            break

    return visible_trees


def find_visible_trees_top(tree_grid, row_index, col_index):
    tree_height = tree_grid[row_index][col_index]
    visible_trees = 0
    for next_row in range(row_index - 1, -1, -1):
        visible_trees += 1
        if tree_grid[next_row][col_index] >= tree_height:
            break

    return visible_trees


def find_visible_trees_bottom(tree_grid, row_index, col_index):
    tree_height = tree_grid[row_index][col_index]
    visible_trees = 0
    for next_row in range(row_index + 1, len(tree_grid)):
        visible_trees += 1
        if tree_grid[next_row][col_index] >= tree_height:
            break

    return visible_trees


def find_tree_scenic_score(tree_grid, row_index, col_index):
    return calculate_scenic_score(
        find_visible_trees_left(tree_grid, row_index, col_index),
        find_visible_trees_right(tree_grid, row_index, col_index),
        find_visible_trees_top(tree_grid, row_index, col_index),
        find_visible_trees_bottom(tree_grid, row_index, col_index),
    )


def calculate_scenic_score(left_score, top_score, right_score, bottom_score):
    return left_score * top_score * right_score * bottom_score


def problem_08_2():
    tree_height_input = read_file("inputs/08_1.txt")

    # Convert input to usable 2D array of digits
    tree_height_grid = convert_input_to_grid(tree_height_input)
    
    highest_scenic_score = 0
    for row_index in range(len(tree_height_grid)):
        for col_index in range(len(tree_height_grid[0])):
            if (score := find_tree_scenic_score(tree_height_grid, row_index, col_index)) > highest_scenic_score:
                highest_scenic_score = score

    return highest_scenic_score
            

print(f"Problem 08 - 1: {problem_08_1()}")
print(f"Problem 08 - 2: {problem_08_2()}")