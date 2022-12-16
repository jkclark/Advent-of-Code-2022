def read_file(file_path):
    with open(file_path) as stream:
        return stream.readlines()