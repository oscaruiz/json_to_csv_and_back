import json
import csv
import argparse

def flatten_json(json_obj, parent_key='', sep='__SEP__'):
    items = []
    for k, v in json_obj.items():
        new_key = f'{parent_key}{sep}{k}' if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_json(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def json_to_csv(json_filepath, csv_filepath, sep='__SEP__'):
    try:
        with open(json_filepath, 'r', encoding='utf-8') as json_file:
            json_data = json.load(json_file)

        flat_data = flatten_json(json_data, sep=sep)

        with open(csv_filepath, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(flat_data.keys())
            writer.writerow(flat_data.values())
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert JSON to CSV")
    parser.add_argument('json_filepath', type=str, help='Path to the input JSON file')
    parser.add_argument('csv_filepath', type=str, help='Path to the output CSV file')
    args = parser.parse_args()
    
    # Convert JSON to CSV
    json_to_csv(args.json_filepath, args.csv_filepath)
