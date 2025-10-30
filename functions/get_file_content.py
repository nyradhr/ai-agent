from os.path import join, abspath, isfile
from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    
    try:
        full_path = abspath(join(working_directory, file_path))
        root_path = abspath(working_directory)

        if not full_path.startswith(root_path):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not isfile(full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(full_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if f.read() != '':
                file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'
            return file_content_string
        
    except Exception as e:
        return f'Error: {e}'
