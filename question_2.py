import json
import os

from data_loader import load_data

project_folder = os.getcwd()
all_data = load_data(project_folder)


def generate_partitioned_jsonl_files(jsonl_dataset, needed_languages, output_folder='answers/question_2'):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Initialize dictionaries to hold datasets for each partition
    partitions = {'test': {}, 'train': {}, 'dev': {}}

    # Iterate over all datasets and categorize them by language and partition
    for data in jsonl_dataset:
        locale = data.get('locale', '').split('-')[0]  # Extract language part from locale
        partition = data.get('partition', '')
        data_id = data.get('id', '')

        if locale in needed_languages and partition in partitions:
            if locale not in partitions[partition]:
                partitions[partition][locale] = []
            partitions[partition][locale].append(data)

    # Write the categorized datasets to separate JSONL files
    for partition, languages_data in partitions.items():
        for language, datasets in languages_data.items():
            filename = os.path.join(output_folder, f'{language}-{partition}.jsonl')
            with open(filename, 'w', encoding='utf-8') as file:
                for data in datasets:
                    file.write(json.dumps(data) + '\n')
            print(f'File {filename} has been created.')


languages = ['en', 'sw', 'de']
generate_partitioned_jsonl_files(all_data, languages)
