#!/usr/bin/python3

import sys
import os
import yaml
import asyncio

from finals import REQUIRED_PYTHON_VER, SUPPORTED_OS


def check_configurations() -> None:
    """Check if the configurations are valid."""
    print("Checking configurations...")
    config_folder = "./configurations"

    # Check if the configurations folder exists
    if not os.path.exists(config_folder) and not os.path.isdir(config_folder):
        print("ERROR: Configurations folder does not exist.")
        exit(1)
    print(f"Configurations Folder found at {config_folder}")

    # Check the YAML files
    print("Checking YAML files...")
    for file in os.listdir(config_folder):
        if file.endswith(".yaml"):
            print(f"Found: {file}")


def check_os() -> None:
    """Check if the right OS is running."""
    print("Checking OS...")
    print(f"OS: {sys.platform}")

    is_supported: bool = False
    for os_name in SUPPORTED_OS:
        if sys.platform == os_name:
            is_supported = True
            break
    if is_supported is False:
        print(f"{sys.platform} is currentely not supported.")
        exit(1)


def check_python() -> None:
    """Check if the right Python version is running."""
    print("Checking Python version...")
    print(f"Python version: {sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}")
    if sys.version_info < REQUIRED_PYTHON_VER:
        print(f"ERROR: Python {REQUIRED_PYTHON_VER[0]}.{REQUIRED_PYTHON_VER[1]}.{REQUIRED_PYTHON_VER[2]} "
              f"or higher is required.")
        exit(1)


def main() -> int:
    """The main function."""
    exit_code: int = 0

    check_python()
    check_os()
    check_configurations()
    # TODO: Check files integrity

    # TODO: Load plugins
    # TODO: Connect to database
    # TODO: Start entity manager
    # TODO: Start event manager
    # TODO: Start task manager

    return exit_code


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    exit(main())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
