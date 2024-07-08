# NDC Prompt Library

## Overview

NDC Prompt Library is a collection of system prompts created based on the Nippon Decimal Classification (NDC) system. This library is organized according to the NDC classification scheme, allowing for efficient management and utilization of prompts across various fields.

## Structure

For detailed information about the library's structure, please refer to [ndc_list.md](ndc_list.md). This file contains a list of prompts organized according to the NDC classification.

## Automatic Directory Structure Generation

This repository includes a Python script called [create_directories.py](create_directories.py). This script has the following features:

- It automatically generates a directory structure based on the contents of the [directory_structure.txt](directory_structure.txt) file (which uses a format commonly seen on platforms like Github) located in the same directory as the script.
- It also automatically generates a `.gitignore` file, making the created directory structure suitable for sharing on Github.

This script was used to create the directory structure for this library, but it can also be used for other projects. Feel free to use it in your own work!

## License

This project is released under the [MISA-RM](LICENSE.md) license. Please make sure to check the license terms before use.

## Contributions

We welcome contributions such as adding or improving prompts, reporting bugs, etc. Please help develop this project through pull requests and issues.

## Contact

If you have any questions or suggestions, please reach out through Github issues.