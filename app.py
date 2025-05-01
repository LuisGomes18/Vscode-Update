from extras.check_paths import check_folder, check_file
from extras.directory_mapping import create_tmp_folder, remove_tmp_folder, remove_content_destination_folder, move_file_to_destination
from extras.check_processes import check_vscode_instances
from extras.download_vscode import download_vscode
from extras.handling_compressed_files import compressed_files
import os
import sys


# Permission check
if os.geteuid() != 0:
    print('[ERROR] This script must be executed as root.')
    sys.exit(1)

# System information
operating_system = os.uname().sysname.lower()
if operating_system not in ['linux', 'darwin', 'windows']:
    print('[ERROR] The operating system is not supported.')
    sys.exit(1)

architecture = os.uname().machine.lower()
filename_without_extension = 'vscode'

print(f'[INFO] Detected system: {operating_system}, Architecture: {architecture}')

# Project paths
project_path = os.getcwd()
relative_tmp_folder_path = '.tmp'
absolute_tmp_folder_path = os.path.join(project_path, relative_tmp_folder_path)

# Prepare temporary folder
if check_folder(absolute_tmp_folder_path):
    print(f'[DEBUG] Removing existing temp folder: {absolute_tmp_folder_path}')
    remove_tmp_folder(absolute_tmp_folder_path)
print(f'[DEBUG] Creating temp folder: {absolute_tmp_folder_path}')
create_tmp_folder(absolute_tmp_folder_path)

# Define filename based on OS
if operating_system == 'linux':
    filename_with_extension = 'vscode.tar.gz'
else:
    filename_with_extension = 'vscode.zip'

# Temporary file paths
tmp_file_with_ext_path = os.path.join(absolute_tmp_folder_path, filename_with_extension)
tmp_file_without_ext_path = os.path.join(absolute_tmp_folder_path, filename_without_extension)

# Destination folder
absolute_destination_path = str(input('[INPUT] Enter the destination folder: '))
while not check_folder(absolute_destination_path):
    print('[ERROR] The folder does not exist.')
    absolute_destination_path = str(input('[INPUT] Enter the destination folder: '))

print(f'[INFO] Destination folder selected: {absolute_destination_path}')

# Check for running VSCode instance
print('[DEBUG] Checking for running VSCode instances...')
check_vscode_instances(operating_system)

# Clean destination folder
print(f'[INFO] Cleaning destination folder: {absolute_destination_path}')
remove_content_destination_folder(absolute_destination_path)

# Download VSCode
print('[INFO] Downloading VSCode...')
download_vscode(operating_system, architecture, filename_with_extension)

# Extract downloaded file
print('[INFO] Extracting downloaded archive...')
compressed_files(operating_system, tmp_file_with_ext_path, tmp_file_without_ext_path)

# Move to destination
print('[INFO] Moving extracted files to destination folder...')
move_file_to_destination(tmp_file_without_ext_path, absolute_destination_path)

# Clean up temporary folder
print(f'[INFO] Removing temporary folder: {tmp_file_without_ext_path}')
remove_tmp_folder(tmp_file_without_ext_path)

print('[SUCCESS] VSCode has been installed successfully!')
