from data_loader import *
from question_1 import *
from question_2 import *


def load_data(project_directory, jsonl_subfolder='1.1/data'):
    jsonl_folder = os.path.join(project_directory, jsonl_subfolder)
    if not os.path.isdir(jsonl_folder):
        raise ValueError('Invalid folder location. Please enter a valid sub-folder name.')
    return read_jsonl_files(jsonl_folder)


def main():
    """declarations"""
    project_folder = os.getcwd()

    """data extraction"""
    logging.info('Select your zipped dataset source')
    selected_file = select_file()
    extracted_folder = os.path.join(project_folder, '1.1')
    try:
        logging.info('Extracting the Data .....')
        dataset_extraction(selected_file, project_folder, extracted_folder)
    except Exception as e:
        print('\n')
        logging.error(f'An error {e} has occurred')
        exit(1)

    all_data = load_data(project_folder)
    """question 1"""
    try:
        print('\n')
        logging.info('Generating en-xx.xlxs files ....')
        generate_excel_files(all_data)

        print('\n')
        logging.info(f'Total number of datasets: {len(all_data)} are present')
    except Exception as e:
        print('\n')
        logging.error(f'An error {e} has occurred')

    """question 2"""
    try:
        print('\n')
        logging.info('Generating for selected languages their train, test and dev files .....')
        languages = ['en', 'sw', 'de']
        generate_partitioned_jsonl_files(all_data, languages)

        print('\n')
        logging.info('The necessary files have been generated')
    except Exception as e:
        print('\n')
        logging.info(f'An error occurred at: {e}')


if __name__ == "__main__":
    main()
