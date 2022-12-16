from utils import read_file


class Directory:
    def __init__(self, parent=None):
        self.parent = parent
        self.size = 0
        # We never actually reference the names of the children directories,
        # so this could just be a list or a tuple or a set, but it's fine...
        self.children = {}
        self.files = []


def parse_directory_files_and_directories(terminal_input, starting_line_index):
    files = []
    directories = []
    curr_line_index = starting_line_index
    line = terminal_input[curr_line_index]
    while not line.startswith("$"):
        # This entry is a child directory
        if line.startswith("dir"):
            child_dir_name = line.split()[-1]
            directories.append(child_dir_name)

        # This entry is a file
        else:
            file_size, file_name = line.split()
            files.append((int(file_size), file_name))

        curr_line_index += 1
        if curr_line_index >= len(terminal_input):
            break
        line = terminal_input[curr_line_index]
        
    return files, directories


def create_filesystem(terminal_input):
    curr_dir = root = Directory()
    curr_line_index = 0
    while curr_line_index < len(terminal_input):
        line = terminal_input[curr_line_index]

        # Listing directory contents
        if line.startswith("$ ls"):  # List command
            # Move past this line
            curr_line_index += 1
            
            files, directories = parse_directory_files_and_directories(
                terminal_input,
                curr_line_index
            )

            curr_dir.files = files
            # Set all children to Directory with parent curr_dir
            for child in directories:
                curr_dir.children[child] = Directory(curr_dir)

            # -1 because we start on the first entry of the list
            # (we want to let the ++ at the bottom of the loop
            # move to the next command line)
            curr_line_index += len(files) + len(directories) - 1

        # Moving back up to parent directory
        elif line.startswith("$ cd .."):
            curr_dir = curr_dir.parent

        # Moving to a child directory
        elif line.startswith("$ cd"):
            next_dir_name = line.split()[-1]
            curr_dir = curr_dir.children[next_dir_name]

        # Error
        else:
            print(f"Somehow saw a line not starting with $: {line}")

        curr_line_index += 1

    return root


def set_directory_sizes(root):
    # DFS approach
    for child in root.children.values():
        set_directory_sizes(child)

    size = 0
    size += sum([file[0] for file in root.files])
    size += sum([dir.size for dir in root.children.values()])
    root.size = size


def problem_07_1():
    terminal_input = read_file("inputs/07_1.txt")[1:]  # Skip "cd /"

    # Parse input to create filesystem DAG
    root = create_filesystem(terminal_input)

    # Iterate through tree and set size of each directory
    set_directory_sizes(root)

    # Iterate through all directories, tracking sum of dirs
    # with size <= 100,000
    MAX_DIR_SIZE = 100_000
    total_small_dir_size = 0
    def dfs_sum_small_dir_sizes(root):
        nonlocal total_small_dir_size

        # Add size to total if dir qualifies
        if root.size <= MAX_DIR_SIZE:
            total_small_dir_size += root.size

        # Recursively call on all child dirs
        for dir in root.children.values():
            dfs_sum_small_dir_sizes(dir)

    dfs_sum_small_dir_sizes(root)
    return total_small_dir_size


def problem_07_2():
    terminal_input = read_file("inputs/07_1.txt")[1:]  # Skip "cd /"

    # Parse input to create filesystem DAG
    root = create_filesystem(terminal_input)

    # Iterate through tree and set size of each directory
    set_directory_sizes(root)

    # Numbers we already have:
    #  - Total filespace available to the system: 70,000,000
    #  - Total used space:                        46,975,962
    #  - Total unused space:                      23,024,038    
    #
    # Numbers given to us in the problem:
    #  - Unused space required for update:        30,000,000
    #
    # 
    # Amount of space required to be cleared:     30,000,000 (space required)
    #                                            -23,024,038 (space already free)
    #                                            -----------
    #                                              6,975,962 (space to be cleared)
    #
    # Therefore, we are looking for the smallest directory
    # with a size greater than or equal to 6,975,962
    SMALLEST_QUALIFYING_DIRECTORY_SIZE = 6_975_962
    size_of_smallest_qualifying_directory = 99_999_999
    def dfs_find_smallest_qualifying_directory(root):
        nonlocal size_of_smallest_qualifying_directory

        # Check to see if this is the best qualifying dir so far
        smallest_yet = root.size < size_of_smallest_qualifying_directory
        big_enough = root.size >= SMALLEST_QUALIFYING_DIRECTORY_SIZE
        if smallest_yet and big_enough:
            size_of_smallest_qualifying_directory = root.size

        # Recursively call on all child dirs
        for dir in root.children.values():
            dfs_find_smallest_qualifying_directory(dir)

    dfs_find_smallest_qualifying_directory(root)
    return size_of_smallest_qualifying_directory


print(f"Problem 07 - 1: {problem_07_1()}")
print(f"Problem 07 - 2: {problem_07_2()}")