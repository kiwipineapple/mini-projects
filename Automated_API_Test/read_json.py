import json


def read_json():
    # Open and read the JSON file
    # ./ bedeutet file von current Ordner. ../ bedeutet file von oberen Ordner.
    try:
        with open('./data.json', 'r', encoding='UTF-8') as file:
            data = json.load(file)
            return data
    except Exception as e:
        print(f"Error: {e}")
