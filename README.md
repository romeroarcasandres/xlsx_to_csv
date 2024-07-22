# XLSX_to_CSV
The script converts Excel (.xlsx) files to comma-separated values (.csv) format.

## Overview:
The XLSX_to_CSV script processes .xlsx files within a specified directory, converting each to a .csv file. This script makes it easier to work with Excel data in various data processing and analysis tools that prefer or require .csv format.

## Requirements:
Python 3
pandas library (for reading and writing Excel and CSV files)
tkinter library (for directory selection dialog)
os library (for file path operations)

## Files
XLSX_to_CSV.py

## Usage
1. Run the script.
2. A directory selection dialog will prompt you to choose a folder containing the .xlsx files you want to convert.
3. After selecting the directory, the script will convert each .xlsx file in the directory to a .csv file.
4. The resulting .csv files will be saved in the same directory with the same name as the original .xlsx files, but with a ".csv" extension.

## Important Note
Ensure that the selected directory contains valid Excel files in .xlsx format.
The script converts all .xlsx files in the chosen directory; ensure there are no irrelevant files to avoid unnecessary conversions.
Unicode encoding (utf-8) is used.

## License
This project is governed by the GNU Affero General Public License v3.0. For comprehensive details, kindly refer to the LICENSE file included with this project.
