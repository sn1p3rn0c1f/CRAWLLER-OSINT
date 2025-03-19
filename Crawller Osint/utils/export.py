import json
import csv
from datetime import datetime
import os

def export_to_json(data, filename_prefix):
    """Export les données en JSON"""
    filename = f"exports/{filename_prefix}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    os.makedirs("exports", exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    print(f"[+] Results exported to {filename}")

def export_to_csv(data, filename_prefix):
    """Export les données en CSV (si format simple)"""
    filename = f"exports/{filename_prefix}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    os.makedirs("exports", exist_ok=True)

    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Category', 'Key', 'Value'])

        for category, values in data.items():
            if isinstance(values, dict):
                for key, val in values.items():
                    writer.writerow([category, key, val])
            elif isinstance(values, list):
                for val in values:
                    writer.writerow([category, '', val])
            else:
                writer.writerow([category, '', values])

    print(f"[+] Results exported to {filename}")
