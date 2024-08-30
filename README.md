# json_to_csv_and_back
Python scripts for converting JSON files to CSV and vice versa, preserving structure. Ideal for simplifying JSON readability and enabling non-technical users to make edits.
## Overview

This repository contains a pair of Python scripts that allow you to convert JSON files to CSV format and vice versa while preserving the structure of the data. These tools are useful if you want to enable non-technical users to easily read a JSON file in a simple tabular format or make changes to it.

### Key Features
- **JSON to CSV Conversion**: Transforms a JSON file into a CSV format, making it easier to understand and edit, especially for users unfamiliar with JSON.
- **CSV to JSON Conversion**: Converts a CSV file back into its original JSON format, maintaining the original data structure.

### Usage

To convert JSON to CSV, run:
python ./json_to_csv.py ./example.json ./generated.csv

To convert CSV to JSON, run:
python ./csv_to_json.py ./example.csv ./generated.json
