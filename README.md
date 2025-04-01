# Vscode Update
[![CodeQL Python Security Scan](https://github.com/LuisGomes18/Vscode-Update/actions/workflows/codeql.yml/badge.svg)](https://github.com/LuisGomes18/Vscode-Update/actions/workflows/codeql.yml)
[![Bandit](https://github.com/LuisGomes18/Vscode-Update/actions/workflows/bandit.yml/badge.svg)](https://github.com/LuisGomes18/Vscode-Update/actions/workflows/bandit.yml)

## Description

Vscode Update is a project that automatically updates Visual Studio Code without the need for manual commands.

## Technologies Used

- Python

## Installation and Setup

1. Clone the repository:

   ```sh
   git clone https://github.com/LuisGomes18/Vscode-Update
   ```

2. Navigate to the project directory:

   ```sh
   cd vscode_update
   ```

3. Run the script with superuser permissions:

   ```sh
   sudo python3 app.py
   ```

## How to Use

1. Make sure the script is executed with sudo.
2. The program will ask for the destination folder where VSCode is installed.
3. It will replace the VSCode folder with the files and folders from the new version.
4. At the end of the process, VSCode will be updated without any additional manual intervention.

## Contribution

If you want to contribute to this project:

1. Fork the repository.
2. Create a branch for your changes:

   ```sh
   git checkout -b my-feature
   ```

3. Make your changes and commit:

   ```sh
   git commit -m "Adding new feature"
   ```

4. Push to the remote repository:

   ```sh
   git push origin my-feature
   ```

5. Open a Pull Request for review.

## License

This project is licensed under the MIT License.

## Contact

For questions or suggestions, contact: <luiscgomes0@gmail.com>
