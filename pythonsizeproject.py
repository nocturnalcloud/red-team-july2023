import os

def get_file_size(tuple_item):
    return tuple_item[1]

# Function to process a single directory path
def process_single_path(dir_path):
    # Expand the directory path to handle the home directory shortcut (~)
    dir_path = os.path.expanduser(dir_path)

    # Dictionary to store files and their sizes
    file_info_dict = {}

    # Iterate directory
    for file_path in os.listdir(dir_path):
        # check if current file_path is a file
        if os.path.isfile(os.path.join(dir_path, file_path)):
            # get file size
            file_size = os.path.getsize(os.path.join(dir_path, file_path))
            # add filename and size to the dictionary
            file_info_dict[file_path] = file_size

    # Sort the dictionary by file size in descending order using the named function
    sorted_file_info = dict(sorted(file_info_dict.items(), key=get_file_size, reverse=True))

    # Print the file name above the sorted dictionary with file sizes
    print(f"Files in {dir_path}:")
    for file_name, file_size in sorted_file_info.items():
        print(f"{file_name} - {file_size} bytes")
    print("\n")

# Prompt the user to input multiple directory paths separated by a comma
input_paths = input('Please input directory paths (separated by comma): ')

# Split the input paths by comma to get individual paths
paths_list = input_paths.split(',')

# Process each directory path
for dir_path in paths_list:
    process_single_path(dir_path.strip())  # Use strip() to remove leading/trailing spaces (if any)
