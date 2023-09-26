import json
import os
import jsonlines

directory = 'data'

# Iterate over all files in the specified directory

for filename in os.listdir(directory):

    if filename.endswith('.jsonl'):
        filepath = os.path.join(directory, filename)

        # print(filepath)
        with jsonlines.open(filepath) as reader:
            for obj in reader:
                print(json.dumps(obj, indent=4))
