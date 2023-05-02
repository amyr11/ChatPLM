import os
import json


def load_json(directory):
    json_files = []
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            json_files.append(directory + '/' + filename)
    return json_files


def load_intent(path):
    with open(path) as file:
        intent_dict = json.load(file)
        print(f'Loaded: {path}')
        return intent_dict


def append_intents(intents):
    all_intents = {'intents': []}
    for i in intents:
        all_intents['intents'].extend(i['intents'])
    return all_intents


def load_data(directory):
    json_files = load_json(directory)
    intents = [load_intent(f) for f in json_files]
    data = append_intents(intents)
    return data
