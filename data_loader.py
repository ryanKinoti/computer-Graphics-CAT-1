import os
import tarfile
import json
import logging
import tkinter as tk
from tkinter import filedialog

logging.basicConfig(level=logging.INFO)


def select_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(title="Select a .tar.gz file", filetypes=[("tar.gz files", "*.tar.gz")])
    root.destroy()

    if not file_path:
        logging.warning("No file selected.")
        return None

    return file_path


def dataset_extraction(file_location, project_folder, extracted_folder):
    if not file_location.endswith('.tar.gz'):
        raise Exception(f"Invalid file type. Kindly ensure {file_location} is a .tar.gz file")

    if os.path.exists(extracted_folder):
        logging.info(f"The folder {extracted_folder} already exists. Skipping extraction.")
    else:
        try:
            with tarfile.open(file_location, 'r:gz') as file:
                file.extractall(project_folder)
            logging.info(f'Contents of {file_location} extracted successfully to {project_folder}')
        except Exception as e:
            logging.error(f'An error {e} has occurred')


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



