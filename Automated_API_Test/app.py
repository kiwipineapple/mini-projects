from read_json import read_json
from pathlib import Path
import os
import logging
import requests
__autor__ = 'Tong'
__time__ = "2025-09-18"
__doc__ = 'Test liveness of API Endpoints'


os.chdir(Path(__file__).parent)


logging.basicConfig(filename="app.log", level=logging.DEBUG,
                    format='%(name)s - %(levelname)s - %(asctime)s- %(filename)s- %(message)s')


def get_API_status(url):
    "Get Endpoints liveness"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f'Request failed. Error is {e}')

    print("Response Code:", response.status_code)

    if response.status_code == 200:
        return "OK"
    else:
        return "Error"


def main():
    "Show liveness of each Endpoint"
    data = read_json()
    for item in data:
        url = item['URL']
        name = item['name']
        status = get_API_status(url)

        logging.debug(f"Status of {name} is {status}")


if __name__ == "__main__":
    logging.info("Application started")
    main()
    logging.info("Application closed")
