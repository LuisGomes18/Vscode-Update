import tarfile
import zipfile
import os


def compressed_files(platform: str, file_path: str, tmp_path: str) -> None:
    def is_within_directory(directory, target):
        abs_directory = os.path.abspath(directory)
        abs_target = os.path.abspath(target)
        return os.path.commonpath([abs_directory]) == os.path.commonpath([abs_directory, abs_target])

    def remove_first_folder(path: str) -> str:
        parts = path.strip("/").split("/")
        return os.path.join(*parts[1:]) if len(parts) > 1 else parts[-1]

    if platform == 'linux':
        try:
            with tarfile.open(file_path, 'r') as tar_ref:
                for member in tar_ref.getmembers():
                    new_name = remove_first_folder(member.name)
                    if not new_name:
                        continue  # ignora a pasta raiz

                    member_path = os.path.join(tmp_path, new_name)
                    if is_within_directory(tmp_path, member_path):
                        member.name = new_name  # sobrescreve caminho interno
                        tar_ref.extract(member, path=tmp_path)
        except Exception as error:
            raise error

    elif platform in ['darwin', 'windows']:
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            for member in zip_ref.infolist():
                if member.is_dir():
                    continue

                new_name = remove_first_folder(member.filename)
                if not new_name:
                    continue

                target_path = os.path.join(tmp_path, new_name)
                os.makedirs(os.path.dirname(target_path), exist_ok=True)

                if is_within_directory(tmp_path, target_path):
                    with zip_ref.open(member) as source, open(target_path, "wb") as target:
                        target.write(source.read())
