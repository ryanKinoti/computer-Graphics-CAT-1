import json
import os
from data_loader import load_data

project_folder = os.getcwd()
all_data = load_data(project_folder)


def generate_translation_json_file(jsonl_dataset, output_folder='answers', output_file='translations.json'):
    # Check if the folder exists, if not, create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Specify the path to the output file
    output_path = os.path.join(output_folder, output_file)

    # Initialize a list to hold the translation JSON objects
    translations = []

    # Iterate over all datasets and filter them based on the partition and locale fields
    for data_list in jsonl_dataset:  # Assuming jsonl_dataset is a list of lists
        for data in data_list:  # Iterate over each item in the inner list
            if not isinstance(data, dict):  # Check if data is not a dictionary
                print(f"Unexpected data type: {type(data)}, value: {data}")
                continue  # Skip to the next iteration

            locale = data.get('locale', '')
            partition = data.get('partition', '')
            data_id = data.get('id', '')
            utt = data.get('utt', '')

            # Check if the dataset is a train set and the locale starts with en-
            if partition == 'train' and locale.startswith('en-'):
                # Create a new JSON object representing the translation and append it to the list
                translation = {
                    'id': data_id,
                    'utt': utt,
                    'translation_locale': locale.split('-')[1]  # Extract the target language part from locale
                }
                translations.append(translation)

    # Write the translation JSON objects to the output file
    with open(output_path, 'w', encoding='utf-8') as file:
        json.dump(translations, file, ensure_ascii=False, indent=4)  # Pretty print the JSON file

    print(f'File {output_path} has been created.')


# Call the function with the jsonl_dataset array
generate_translation_json_file(all_data)
