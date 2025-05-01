from extras.check_paths import check_folder, check_file
from extras.directory_mapping import create_tmp_folder, remove_tmp_folder, remove_content_destination_folder, move_file_to_destination
from extras.check_processes import check_vscode_instances
from extras.download_vscode import download_vscode
from extras.handling_compressed_files import compressed_files
import os


if not os.geteuid() == 0:
    print('The file must be executed as root')
    exit(1)

# System Information
operating_system = os.uname().sysname.lower()
if operating_system not in ['linux', 'darwin', 'windows']:
    print('The system used is not supported by the project.')
    exit(1)
architecture = os.uname().machine.lower()
filename_without_extension = 'vscode'

# Folder Information
project_path = os.getcwd()
relative_tmp_folder_path = '.tmp'
absolute_tmp_folder_path = os.path.join(project_path, relative_tmp_folder_path)
if check_folder(absolute_tmp_folder_path):
    remove_tmp_folder(absolute_tmp_folder_path)
create_tmp_folder(absolute_tmp_folder_path)

# File Information
filename_with_extension = None

if operating_system == 'linux':
    filename_with_extension = 'vscode.tar.gz'
elif operating_system == 'windows':
    filename_with_extension = 'vscode.zip'
elif operating_system == 'darwin':
    filename_with_extension = 'vscode.zip'

# Temporary paths and folders
tmp_file_with_ext_path = os.path.join(absolute_tmp_folder_path, filename_with_extension)  # type: ignore
tmp_file_without_ext_path = os.path.join(absolute_tmp_folder_path, filename_without_extension)

# Destination path and folders
absolute_destination_path = str(input('Write the destination folder: '))
folder_check = check_folder(absolute_destination_path)
while not folder_check:
    absolute_destination_path = str(input('Write the destination folder: '))
    folder_check = check_folder(absolute_destination_path)


# check_vscode_instances(operating_system)
remove_content_destination_folder(absolute_destination_path)
download_vscode(operating_system, architecture, filename_with_extension)

compressed_files(operating_system, tmp_file_with_ext_path, tmp_file_without_ext_path)

move_file_to_destination(tmp_file_without_ext_path, absolute_destination_path)
remove_tmp_folder(tmp_file_without_ext_path)
