def get_file_type(file_attribute: str) -> str:
    file_type_dict = {
        '-': "file",
        'd': "directory",
        'l': "symlink",
        'c': "character_file",
        'b': "block_file",
        'p': "pipe",
        's': "socket",
        'D': "door"
    }
    # Return the file type based on the first character of the file_attribute
    return file_type_dict[file_attribute[0]]

