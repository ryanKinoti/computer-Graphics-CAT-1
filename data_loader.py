import os
import tarfile
import json

"""Extraction of the zipp files and sorting everything out"""

file_location = 'CAT-dataset.tar.gz'
project_folder = os.getcwd()
extracted_folder = os.path.join(project_folder, '1.1')

if not os.path.isfile(file_location):
    print("Invalid file location. Please enter a valid tar.gz file location.")
    exit(1)

if not file_location.endswith('.tar.gz'):
    print("Invalid file type. Please enter a valid tar.gz file.")
    exit(1)

if os.path.exists(extracted_folder):
    print(f"The folder {extracted_folder} already exists. Skipping extraction.")
else:
    try:
        # Open the tar.gz file in read mode
        with tarfile.open(file_location, 'r:gz') as file:
            # Extract all contents into the project folder
            file.extractall(project_folder)
        print(f"Contents extracted successfully to {project_folder}")
    except Exception as e:
        print(f"An error occurred while extracting the file: {e}")


def read_jsonl_files(directory):
    data = []
    filenames = []

    # List all files in the specified directory
    for filename in os.listdir(directory):

        # Check if the file has a .jsonl extension
        if filename.endswith('.jsonl'):
            filepath = os.path.join(directory, filename)
            filenames.append(filename)

            # Open each jsonl file and read its contents
            with open(filepath, 'r', encoding='utf-8') as file:
                for line in file:
                    # Parse each line as a JSON object and append it to the data list
                    data.append(json.loads(line))
    return data


def load_data(project_directory, jsonl_subfolder='1.1/data'):
    jsonl_folder = os.path.join(project_directory, jsonl_subfolder)
    if not os.path.isdir(jsonl_folder):
        raise ValueError("Invalid folder location. Please enter a valid sub-folder name.")
    return read_jsonl_files(jsonl_folder)
