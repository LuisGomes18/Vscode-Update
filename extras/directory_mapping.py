import os
import shutil 


def crate_tmp_folder(tmp_path: str) -> None:
    try:
        os.makedirs(tmp_path, exist_ok=True)
        os.chdir(tmp_path)
    except Exception as error:
        raise error

def remove_tmp_folder(tmp_path: str) -> None:
    try:
        shutil.rmtree(tmp_path)
    except Exception as error:
        raise error

def remove_content_destination_folder(destination_path: str) -> None:
    for item in os.listdir(destination_path):
        item_path = os.path.join(destination_path, item)
        try:
            if os.path.isfile(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
        except Exception as error:
            raise error


def move_file_to_destination(tmp_path: str, destination_path: str) -> None:
    try:
        for item in os.listdir(tmp_path):
            item_path = os.path.join(tmp_path, item)
            item_destination_path = os.path.join(destination_path, item)
            shutil.move(item_path, item_destination_path)
    except Exception as error:
        raise error
