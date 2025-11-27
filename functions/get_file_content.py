import os
import functions.config as config

def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_fil = os.path.abspath(os.path.join(working_directory, file_path))
    print(abs_working_dir)
    print(target_fil)
    if not target_fil.startswith(abs_working_dir):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_fil):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    

    with open(target_fil, "r") as f:
        file_content_string = f.read(config.MAX_CHARS)
        if config.MAX_CHARS == len(file_content_string):
            file_content_string = file_content_string+ f'...File "{target_fil}" truncated at 10000 characters'
        return file_content_string
    