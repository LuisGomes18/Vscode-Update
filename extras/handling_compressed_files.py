import tarfile
import zipfile
import os


def compressed_files(platform: str, file_path: str, tmp_path: str) -> None:
    def is_within_directory(directory: str, target: str) -> bool:
        abs_directory = os.path.abspath(directory)
        abs_target = os.path.abspath(target)
        return os.path.commonpath([abs_directory]) == os.path.commonpath([abs_directory, abs_target])

    def remove_first_folder(path: str) -> str:
        parts = path.strip('/').split('/')
        return os.path.join(*parts[1:]) if len(parts) > 1 else parts[-1]

    print(f'[DEBUG] Extracting file: {file_path}')
    print(f'[DEBUG] Target temporary path: {tmp_path}')
    print(f'[DEBUG] Platform detected: {platform}')

    if platform == 'linux':
        try:
            with tarfile.open(file_path, 'r:*') as tar_ref:
                print('[INFO] TAR archive opened successfully.')
                for member in tar_ref.getmembers():
                    new_name = remove_first_folder(member.name)
                    if not new_name:
                        print(f'[DEBUG] Skipping root folder: {member.name}')
                        continue

                    member_path = os.path.join(tmp_path, new_name)
                    if is_within_directory(tmp_path, member_path):
                        member.name = new_name  # override internal path
                        tar_ref.extract(member, path=tmp_path)
                        print(f'[INFO] Extracted: {new_name}')
                    else:
                        print(f'[WARNING] Skipped file outside target directory: {member.name}')
        except Exception as error:
            print(f'[ERROR] Failed to extract TAR archive: {error}')
            raise

    elif platform in ['darwin', 'windows']:
        try:
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                print('[INFO] ZIP archive opened successfully.')
                for member in zip_ref.infolist():
                    if member.is_dir():
                        print(f'[DEBUG] Skipping directory: {member.filename}')
                        continue

                    new_name = remove_first_folder(member.filename)
                    if not new_name:
                        print(f'[DEBUG] Skipping empty or root file: {member.filename}')
                        continue

                    target_path = os.path.join(tmp_path, new_name)
                    if is_within_directory(tmp_path, target_path):
                        os.makedirs(os.path.dirname(target_path), exist_ok=True)
                        with zip_ref.open(member) as source, open(target_path, 'wb') as target:
                            target.write(source.read())
                        print(f'[INFO] Extracted: {new_name}')
                    else:
                        print(f'[WARNING] Skipped file outside target directory: {member.filename}')
        except Exception as error:
            print(f'[ERROR] Failed to extract ZIP archive: {error}')
            raise

    else:
        print(f'[ERROR] Unsupported platform: {platform}')
        raise ValueError(f'Unsupported platform: {platform}')
