import os
import shutil


def create_tmp_folder(tmp_path: str) -> None:
    print(f'[INFO] Creating temporary folder at: {tmp_path}')
    os.makedirs(tmp_path, exist_ok=True)
    os.chdir(tmp_path)
    print(f'[INFO] Current working directory set to: {os.getcwd()}')


def remove_tmp_folder(tmp_path: str) -> None:
    if os.path.exists(tmp_path):
        print(f'[INFO] Removing temporary folder: {tmp_path}')
        shutil.rmtree(tmp_path)
        print(f'[INFO] Temporary folder removed successfully: {tmp_path}')
    else:
        print(f'[WARNING] Temporary folder does not exist: {tmp_path}')


def remove_content_destination_folder(destination_path: str) -> None:
    if not os.path.exists(destination_path):
        print(f'[WARNING] Destination path does not exist: {destination_path}')
        return

    print(f'[INFO] Removing contents of the destination folder: {destination_path}')
    for item in os.listdir(destination_path):
        item_path = os.path.join(destination_path, item)
        try:
            if os.path.isfile(item_path):
                os.remove(item_path)
                print(f'[INFO] File removed: {item_path}')
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
                print(f'[INFO] Directory removed: {item_path}')
        except Exception as error:
            print(f'[ERROR] Failed to remove {item_path}: {error}')
            raise


def move_file_to_destination(tmp_path: str, destination_path: str) -> None:
    if not os.path.exists(destination_path):
        print(f'[INFO] Creating destination folder: {destination_path}')
        os.makedirs(destination_path, exist_ok=True)

    print(f'[INFO] Moving files from {tmp_path} to {destination_path}')
    for item in os.listdir(tmp_path):
        item_path = os.path.join(tmp_path, item)
        item_destination_path = os.path.join(destination_path, item)
        try:
            shutil.move(item_path, item_destination_path)
            print(f'[INFO] Moved: {item_path} -> {item_destination_path}')
        except Exception as error:
            print(f'[ERROR] Failed to move {item_path}: {error}')
            raise
