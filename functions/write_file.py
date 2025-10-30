from os.path import abspath, join, exists

def write_file(working_directory, file_path, content):

    try:
        full_path = abspath(join(working_directory, file_path))
        root_path = abspath(working_directory)

        if not full_path.startswith(root_path):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        mode = 'a'
        if not exists(full_path):
            mode = 'w'
        with open(full_path, mode) as file:
            file.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        
    except Exception as e:
        return f'Error: {e}'