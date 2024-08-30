import json
import csv
import argparse

def unflatten_dict(flat_dict, sep='__SEP__'):
    json_data = {}
    for key, value in flat_dict.items():
        keys = key.split(sep)
        current = json_data
        for k in keys[:-1]:
            if k not in current or not isinstance(current[k], dict):
                current[k] = {}
            current = current[k]
        current[keys[-1]] = value
    return json_data

def csv_to_json(csv_filepath, json_filepath, sep='__SEP__'):
    try:
        with open(csv_filepath, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            header = next(reader)  # Read the header row
            values = next(reader)  # Read the values row

        flat_data = dict(zip(header, values))

        json_data = unflatten_dict(flat_data, sep=sep)

        with open(json_filepath, 'w', encoding='utf-8') as json_file:
            json.dump(json_data, json_file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert CSV to JSON")
    parser.add_argument('csv_filepath', type=str, help='Path to the input CSV file')
    parser.add_argument('json_filepath', type=str, help='Path to the output JSON file')
    args = parser.parse_args()
    
    # Convert CSV back to JSON
    csv_to_json(args.csv_filepath, args.json_filepath)
