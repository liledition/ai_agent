# functions/get_file_content.py

import os
from functions.config import MAX_FILE_SIZE

def get_file_content(working_directory, file_path):
    # Get absolute paths
    working_directory = os.path.abspath(working_directory)
    file_path = os.path.abspath(os.path.join(working_directory, file_path))

    # Check if the file_path is outside the working_directory
    if not file_path.startswith(working_directory + os.sep):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    # Check if the file_path is a regular file
    if not os.path.isfile(file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(file_path, 'r') as file:
            content = file.read()
            # Truncate if longer than CHAR_LIMIT
            if len(content) > MAX_FILE_SIZE:
                return content[:MAX_FILE_SIZE] + f' [...File "{file_path}" truncated at {MAX_FILE_SIZE} characters]'
            return content
    except Exception as e:
        return f'Error: {str(e)}'