import json
import os
from collections import defaultdict

import pandas as pd

from data_loader import load_data

project_folder = os.getcwd()
all_data = load_data(project_folder)
path = 'answers/question_1'
os.makedirs(path, exist_ok=True)


def generate_excel_files(jsonl_dataset):
    # Dictionary to store English datasets
    english_data = {}
    # Dictionary to store non-English datasets grouped by language
    other_languages_data = defaultdict(list)

    # Iterate over all datasets and categorize them
    for data in jsonl_dataset:
        locale = data.get('locale', '')
        data_id = data.get('id', '')
        utt = data.get('utt', '')
        annot_utt = data.get('annot_utt', '')

        if 'en' in locale.lower():
            english_data[data_id] = {'utt': utt, 'annot_utt': annot_utt}
        else:
            language = locale.split('-')[0]  # Extract language part from locale
            other_languages_data[language].append({'id': data_id, 'utt': utt, 'annot_utt': annot_utt})

    # For each non-English language, create an Excel file with matching English datasets
    for language, datasets in other_languages_data.items():
        rows = []
        for data in datasets:
            data_id = data['id']
            if data_id in english_data:
                row = {
                    'id': data_id,
                    f'en_utt': english_data[data_id]['utt'],
                    f'en_annot_utt': english_data[data_id]['annot_utt'],
                    f'{language}_utt': data['utt'],
                    f'{language}_annot_utt': data['annot_utt'],
                }
                rows.append(row)

        if rows:
            df = pd.DataFrame(rows)
            filename = os.path.join(path, f'en-{language}.xlsx')
            df.to_excel(filename, index=False)
            print(f'File {filename} has been created.')


generate_excel_files(all_data)

# """a simple print output to see the dataset arrangements"""
# try:
#     all_data = load_data(project_folder)
#     # Now you can use the all_data array in this file
#     if len(all_data) >= 3:
#         # Print the first 3 elements of the list
#         print(f"First 3 of {len(all_data)} elements of the array:")
#         for i in range(3):
#             print(json.dumps(all_data[i], indent=4))
#     else:
#         print(f"There are less than 3 elements in the array. Total elements: {len(all_data)}")
#         # Print all available elements in the list
#         for element in all_data:
#             print(json.dumps(element, indent=4))
# except ValueError as e:
#     print(e)
