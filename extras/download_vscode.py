import subprocess
import sys


def download_vscode(os_type: str, architecture: str, file_name: str) -> None:
    try:
        print(f'[DEBUG] Preparing to download VSCode for OS: {os_type}, Architecture: {architecture}')

        url = ''
        
        if os_type == 'linux':
            if architecture == 'x86_64':
                url = 'https://code.visualstudio.com/sha/download?build=stable&os=linux-x64'
            elif architecture == 'aarch64':
                url = 'https://code.visualstudio.com/sha/download?build=stable&os=linux-arm64'
            elif architecture == 'aarch32':
                url = 'https://code.visualstudio.com/sha/download?build=stable&os=linux-armhf'
            else:
                print(f'[ERROR] Unsupported architecture for Linux: {architecture}')
                sys.exit(1)

        elif os_type == 'darwin':
            url = 'https://code.visualstudio.com/sha/download?build=stable&os=darwin-arm64'

        elif os_type == 'windows':
            url = 'https://code.visualstudio.com/sha/download?build=stable&os=win32-arm64-archive'

        else:
            print(f'[ERROR] Unsupported operating system: {os_type}')
            sys.exit(1)

        print(f'[INFO] Downloading VSCode from URL: {url}')
        subprocess.run(
            ['wget', '-O', file_name, url],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True
        )
        print(f'[INFO] VSCode downloaded successfully to: {file_name}')

    except subprocess.CalledProcessError as error:
        print(f'[ERROR] Failed to download VSCode. wget error: {error.stderr.decode()}')
        sys.exit(1)
