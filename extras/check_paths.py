import os


def check_folder(folder_path: str) -> bool:
    return os.path.isdir(folder_path)

def check_file(file_path: str) -> bool:
    return os.path.is_file(file_path)
