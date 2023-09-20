[![build status](https://github.com/kleo-53/trik-studio-pioneer-tool/actions/workflows/tox-testing.yml/badge.svg)](https://github.com/kleo-53/trik-studio-pioneer-tool/actions/workflows/tox-testing.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Release (latest by date)](https://img.shields.io/badge/release-v1.0.0--alpha-blue)](https://github.com/kleo-53/trik-studio-pioneer-tool/releases/latest)

# TRIK Studio Pioneer Tool
Companion tool for [TRIK Studio](https://dl.trikset.com/ts/fresh) to simplify the process of uploading programs to Pioneer quadcopter.

This tool provides an executable file ("pioneer-uploader.exe") that integrates with TRIK Studio.

# For users
These simple steps will guide you through setting up and using the TRIK Studio Pioneer Tool.

## Installation
*Before you begin, make sure you have [TRIK Studio](https://dl.trikset.com/ts/fresh) installed on your machine.*
1. Go to the [Releases section](https://github.com/kleo-53/trik-studio-pioneer-tool/releases) of this repository.
2. Download the "pioneer-uploader.exe" file from the latest release.
3. Place the downloaded "pioneer-uploader.exe" file **in the directory where you have TRIK Studio installed**.

## How to use
1. Open TRIK Studio.
2. Create or open your project.
3. When you're ready to upload your program to the quadcopter, simply click the "Upload" button.
The TRIK Studio Pioneer Tool will automatically launch and load the program.

## Alternative
If errors continue to occur while using this tool, please try an **alternative way to upload the program** to the quadcopter: install and use the [Pioneer station](https://docs.geoscan.aero/ru/master/programming/pioneer_station/pioneer_station_main.html) program.

# For developers
You can build the executable file by yourself or run tests locally.

## Prerequisites
To build the project on your system you will need the following tools:
1. **Python**: Make sure you have Python version 3.8 or higher installed on your system. You can download Python from the [official website](https://www.python.org/).
2. **Git**: If you don't have Git, you can install it:
   * On Windows - from the [official site](https://gitforwindows.org/);
   * On linux - with the following command:
   ```
   sudo apt-get install git
   ```

## Installation
0. Open Command Prompt.
1. Clone repository:
   ```
   git clone https://github.com/kleo-53/trik-studio-pioneer-tool.git
   ```
2. Go to the project directory:
   ```
   cd trik-studio-pioneer-tool
   ```
3. Create virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate virtual environment:
   * Windows
   ```bash
   venv\Scripts\activate
   ```
   * Linux
   ```bash
   . venv/bin/activate
   ```
5. Update `pip` and install the necessary packages
   ```bash
   python.exe -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

Now you can edit the project, build the executable file or run tests locally!

## Build executable
1. Install PyInstaller using `pip`:
   ```
   pip install pyinstaller
   ```
2. Build the project using PyInstaller:
   ```
   pyinstaller --onefile --name=pioneer-uploader pioneer_uploader.py
   ```
3. You will find the "pioneer-uploader.exe" file in the **dist** directory.

## Running Tests
You can run tests to ensure the tool's functionality. Tests are available in the "test_uploader.py" file.

### Manual Testing
Run tests with pytest module.
1. Install pytest via `pip`:
   ```
   pip install pytest
   ```
2. Run the tests using the following command:
   ```
   pytest test_uploader.py
   ```

### Using Tox
Alternatively, you can use Tox for testing.
1. Install Tox via `pip`:
   ```
   pip install tox
   ```
2. Run Tox:
   ```
   tox
   ```

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt) site for more details.

## Contributing
Have suggestions or improvements for the TRIK Studio Pioneer Tool? Open an [issue](https://github.com/trikset/trik-studio-pioneer-tool/issues) in our repository. We appreciate your feedback and contributions!