import requests
import logging
import os
from pathlib import Path
from read_json import read_json

os.chdir(Path(__file__).parent)


logging.basicConfig(filename="app.log", level=logging.DEBUG,
                    format='%(name)s - %(levelname)s - %(asctime)s- %(filename)s- %(message)s')


def get_API_status(url):
    response = requests.get(url)
    # data = response.json()

    print("Response Code:", response.status_code)

    if response.status_code == 200:
        return "OK"
    else:
        return "Error"


def main():
    logging.info("Application started")

    data = read_json()
    for item in data:
        url = item['URL']
        name = item['name']
        status = get_API_status(url)

        logging.debug(f"Status of {name} is {status}")

    logging.info("Application closed")


if __name__ == "__main__":
    main()
