import subprocess
import sys


def check_vscode_instances(os_type: str) -> None:
    try:
        print(f'[DEBUG] Checking for running VSCode instances on OS: {os_type}')

        if os_type.lower() == 'windows':
            print('[DEBUG] Using tasklist to check for VSCode on Windows...')
            result = subprocess.run(
                ['tasklist', '/FI', 'IMAGENAME eq Code.exe'],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
            )

            if 'Code.exe' in result.stdout:
                print('[WARNING] An instance of VSCode is running on Windows.')
                print('Please close VSCode and run the script again.')
                sys.exit(1)
            else:
                print('[DEBUG] No VSCode process found on Windows.')

        else:
            print('[DEBUG] Using pgrep to check for VSCode on Unix-like OS...')
            result = subprocess.run(
                ['pgrep', '-x', 'code'],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
            )

            if result.stdout.strip() != '':
                print('[WARNING] An instance of VSCode is running.')
                print('Please close VSCode and run the script again.')
                sys.exit(1)
            else:
                print('[DEBUG] No VSCode process found on Unix-like system.')

    except Exception as error:
        print(f'[ERROR] Failed to check VSCode instance. Exception: {error}')
        sys.exit(1)
