import subprocess


def download_vscode(os: str, architecture: str, file_name: str) -> None:
    try:
        if os == 'linux' and architecture == 'x86_64':
            subprocess.run(
            ['wget', '-O', file_name, 'https://code.visualstudio.com/sha/download?build=stable&os=linux-x64'],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True
            )
        elif os == 'linux' and architecture == 'aarch64':
            subprocess.run(
            ['wget', '-O', file_name, 'https://code.visualstudio.com/sha/download?build=stable&os=linux-arm64'],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True
            )
        elif os == 'linux' and architecture == 'aarch32':
            subprocess.run(
            ['wget', '-O', file_name, 'https://code.visualstudio.com/sha/download?build=stable&os=linux-armhf'],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True
            )
        elif os == 'darwin':
            subprocess.run(
            ['wget', '-O', file_name, 'https://code.visualstudio.com/sha/download?build=stable&os=darwin-arm64'],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True
            )
        elif os == 'windows':
            subprocess.run(
            ['wget', '-O', file_name, 'https://code.visualstudio.com/sha/download?build=stable&os=win32-arm64-archive'],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True
            )
    except subprocess.CalledProcessError as error:
        print(f'ERROR when running the wget: {error.stderr.decode()}')
        exit(1)
