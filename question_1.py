import json
import os

from data_loader import load_data

project_folder = os.getcwd()

try:
    all_data = load_data(project_folder)
    # Now you can use the all_data array in this file
    if len(all_data) >= 3:
        # Print the first 3 elements of the list
        print(f"First 3 of {len(all_data)} elements of the array:")
        for i in range(3):
            print(json.dumps(all_data[i], indent=4))
    else:
        print(f"There are less than 3 elements in the array. Total elements: {len(all_data)}")
        # Print all available elements in the list
        for element in all_data:
            print(json.dumps(element, indent=4))
except ValueError as e:
    print(e)
