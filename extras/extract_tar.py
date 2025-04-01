import os
import tarfile

def extract_tar(tar, path, members=None):
    for member in tar.getmembers():
        if os.path.isabs(member.name) or member.name.startswith(".."):
            raise tarfile.ExtractError("Attempted to extract an absolute path or a path with '..'")
        
        extracted_path = os.path.join(path, member.name)
        if not extracted_path.startswith(path):
            raise tarfile.ExtractError("Attempted to extract outside of the target directory")

        tar.extract(member, path)
