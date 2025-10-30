from os import listdir
from os.path import join, abspath, isdir, basename, getsize


def get_files_info(working_directory, directory="."):

    try:
        full_path = abspath(join(working_directory, directory))
        root_path = abspath(working_directory)

        if not full_path.startswith(root_path):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not isdir(full_path):
            return f'Error: "{directory}" is not a directory'
        
        items = listdir(full_path)
        result = ''
        for item in items:
            item_path = join(full_path, item)
            result += f'- {basename(item_path)}: file_size={getsize(item_path)} bytes, is_dir={isdir(item_path)}\n'
        return result

    except Exception as e:
        return f'Error: {e}'