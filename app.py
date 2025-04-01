import time
import os
import subprocess
import shutil
import tarfile
import zipfile


if not os.geteuid() == 0:
    print('The file must be executed as root')
    exit(1)

system_os = os.uname().sysname.lower()
architecture = os.uname().machine.lower()

project_path = os.getcwd()
file_name_without_extension = "VSCode"
temporary_paste = '.tmp'

if system_os == 'linux':
    file_name_with_extension = "vscode-linux.tar.gz"
    absolute_path_temporary_folder = f'{project_path}/{temporary_paste}'
    absolute_file_path_with_extension = f'{absolute_path_temporary_folder}/{file_name_with_extension}'
    absolute_path_file_without_extension = f'{absolute_path_temporary_folder}/{file_name_without_extension}'
elif system_os == 'darwin':
    file_name_with_extension = 'vscode-mac.zip'
    absolute_path_temporary_folder = f'{project_path}/{temporary_paste}'
    absolute_file_path_with_extension = f'{absolute_path_temporary_folder}/{file_name_with_extension}'
    absolute_path_file_without_extension = f'{absolute_path_temporary_folder}/{file_name_without_extension}'
elif system_os == 'windows':
    file_name_with_extension = 'vscode-windows.zip'
    absolute_path_temporary_folder = f'{project_path}\\{temporary_paste}'
    absolute_file_path_with_extension = f'{absolute_path_temporary_folder}\\{file_name_with_extension}'
    absolute_path_file_without_extension = f'{absolute_path_temporary_folder}\\{file_name_without_extension}'
else:
    print('Unknown system')
    exit(1)

absolute_destination_path = str(input('Enter the destination path: '))
while absolute_destination_path is None:
    absolute_destination_path = str(input('Enter the destination path: '))

while not os.path.isdir(absolute_destination_path):
    print('Destination folder does not exist')
    absolute_destination_path = str(input('Enter the destination path: '))

try:
    if system_os == 'windows':
        result = subprocess.run(['tasklist', '/FI', '"IMAGENAME eq Code.exe"'], stdout=subprocess.PIPE, text=True)
        if result.stdout.strip() != "":
            print('An instance of VSCode is running. Please close VSCode and run the script again.')
            exit(1)

    result = subprocess.run(['pgrep', '-x', 'code'], stdout=subprocess.PIPE, text=True)
    if result.stdout.strip() != "":
        print('An instance of VSCode is running. Please close VSCode and run the script again.')
        exit(1)
except Exception as error:
    print(f'Error when checking if there is an instance of running VSCode. Error: {error}')
    exit(1)

try:
    print('Creating folder .TMP if it doesn\'t exist')
    os.makedirs(absolute_path_temporary_folder, exist_ok=True)
    os.chdir(absolute_path_temporary_folder)
except Exception as error:
    print(f'Error when trying to create or move to the .tmp folder: {error}')
    exit(1)

if os.path.exists(absolute_file_path_with_extension):
    print('Removing VSCode file from temporary folder')
    try:
        os.remove(absolute_file_path_with_extension)
        time.sleep(5)
    except:
        pass

if os.path.exists(absolute_path_file_without_extension):
    print('Removing extracted VSCode folder from temporary folder')
    try:
        shutil.rmtree(absolute_path_file_without_extension)
        time.sleep(5)
    except:
        pass

try:
    print('Downloading the VSCode file')
    if system_os == 'linux' and architecture == 'x86_64':
        result = subprocess.run(
            ['wget', '-O', file_name_with_extension, 'https://code.visualstudio.com/sha/download?build=stable&os=linux-x64'],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True
        )
    elif system_os == 'linux' and architecture == 'aarch64':
        result = subprocess.run(
            ['wget', '-O', file_name_with_extension, 'https://code.visualstudio.com/sha/download?build=stable&os=linux-arm64'],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True
        )
    elif system_os == 'linux' and architecture == 'aarch32':
        result = subprocess.run(
            ['wget', '-O', file_name_with_extension, 'https://code.visualstudio.com/sha/download?build=stable&os=linux-armhf'],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True
        )
    elif system_os == 'darwin':
        result = subprocess.run(
            ['wget', '-O', file_name_with_extension, 'https://code.visualstudio.com/sha/download?build=stable&os=darwin-arm64'],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True
        )
    elif system_os == 'windows':
        result = subprocess.run(
            ['wget', '-O', file_name_with_extension, 'https://code.visualstudio.com/sha/download?build=stable&os=win32-arm64-archive'],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True
        )
except subprocess.CalledProcessError as error:
    print(f'ERROR when running the wget: {error.stderr.decode()}')
    exit(1)

print('Extracting the VSCode file')
if system_os == 'linux':
    with tarfile.open(absolute_file_path_with_extension, 'r:gz') as tar:
        members = tar.getnames()
        if members:
            root_folder = os.path.commonprefix(members)
            destination_tmp = os.path.join(absolute_path_temporary_folder, "VSCode")
            tar.extractall(path=absolute_path_temporary_folder)
            os.rename(os.path.join(absolute_path_temporary_folder, root_folder), destination_tmp)
elif system_os in ['darwin', 'windows']:
    with zipfile.ZipFile(absolute_file_path_with_extension, 'r') as zip_ref:
        members = zip_ref.namelist()
        if members:
            root_folder = os.path.commonprefix(members)
            destination_tmp = os.path.join(absolute_path_temporary_folder, "VSCode")
            zip_ref.extractall(path=absolute_path_temporary_folder)
            os.rename(os.path.join(absolute_path_temporary_folder, root_folder), destination_tmp)


print('Removing files and folders from the destination folder')
for item in os.listdir(absolute_destination_path):
    caminho_item = os.path.join(absolute_destination_path, item)
    if os.path.isfile(caminho_item):
        os.remove(caminho_item)
    elif os.path.isdir(caminho_item):
        shutil.rmtree(caminho_item)

print('Moving files to the destination folder')
for item in os.listdir(absolute_path_file_without_extension):
    caminho_item = os.path.join(absolute_path_file_without_extension, item)
    item_destino = os.path.join(absolute_destination_path, item)

    shutil.move(caminho_item, item_destino)

try:
    time.sleep(10)
    print('Removing .tmp folder')
    shutil.rmtree(absolute_path_temporary_folder)
except FileNotFoundError:
    print('Folder .tmp not found')
    exit(1)
except PermissionError:
    print('Permission denied to remove the folder')
    exit(1)
