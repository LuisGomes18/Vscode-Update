import subprocess


def check_vscode_instances(os: str) -> None:
    try:
        if os == 'windows':
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
