[![build status](https://github.com/kleo-53/trik-studio-pioneer-tool/actions/workflows/tox-testing.yml/badge.svg)](https://github.com/kleo-53/trik-studio-pioneer-tool/actions/workflows/tox-testing.yml)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![GitHub Release (latest by date)](https://img.shields.io/github/v/release/kleo-53/trik-studio-pioneer-tool)](https://img.shields.io/github/v/release/kleo-53/trik-studio-pioneer-tool)

# Trik Studio Pioneer Tool
Companion tool for [TRIK Studio](https://dl.trikset.com/ts/fresh) to simplify the process of uploading programs to Pioneer quadcopter.

This tool provides an executable file (pioneer-uploader.exe) that integrates with Trik Studio.

# For users
These simple steps will guide you through setting up and using the Trik Studio Pioneer Tool.

## Installation
*Before you begin, make sure you have [TRIK Studio](https://dl.trikset.com/ts/fresh) installed on your machine.*
1. Go to the [Releases section](https://github.com/kleo-53/trik-studio-pioneer-tool/releases) of this repository.
2. Download the pioneer-uploader.exe file from the latest release.
3. Place the downloaded pioneer-uploader.exe file **in the directory where you have Trik Studio installed**.

## How to use
1. Open Trik Studio.
2. Create or open your project.
3. When you're ready to upload your program to the quadcopter, simply click the "Upload" button.
The Trik Studio Pioneer Tool will automatically launch and load the program to the quadcopter.

# For developers

## Installation
*Before you begin, make sure you have [Python](https://www.python.org/) (version 3.8 or higher) installed on your system.*
1. Clone repository.
2. Create virtual environment:
```bash
python -m venv venv
```
3. Activate virtual environment:
Windows
```bash
venv\Scripts\activate
```

Linux
```bash
. venv/bin/activate
```
4. Upgrade pip and install requirements:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
5. Run file with uploading program:
```bash
. venv/bin/activate
```

## Prerequisites

## Running Tests
You can run tests to ensure the tool's functionality. Tests are available in the test_uploader.py file.

### Manual Testing
Make sure you have pytest installed. You can install it via pip:

```bash
> pip install pytest
```
Run the tests using the following command:

```bash
> pytest test_uploader.py
```

### Using Tox
Alternatively, you can use Tox for testing. Install Tox via pip:
```bash
> pip install tox
```

Then, simply run Tox:
```bash
> tox
```

## License
This project is licensed under the Apache License 2.0 - see the [LICENSE](https://www.apache.org/licenses/LICENSE-2.0) site for more details.

## Contributing
Have suggestions or improvements for the Trik Studio Pioneer Tool? Open an [issue](https://github.com/trikset/trik-studio-pioneer-tool/issues) in our repository. We appreciate your feedback and contributions!

