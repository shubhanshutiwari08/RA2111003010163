import requests
import json
import logging


logging.basicConfig(level=logging.INFO)


def request_for_authorize(url, data):
    try:
        response = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error("Error making POST request: %s", e)
        return None


def responseSave(response, notebook_filename):
    try:
        with open(notebook_filename, 'w') as notebook_file:
            json.dump(response, notebook_file, indent=4)
        logging.info("Response saved to %s", notebook_filename)
    except IOError as e:
        logging.error("Error saving response to notebook: %s", e)


def main():
    url = "http://20.244.56.144/test/auth"
    data = {
        "companyName": "Meraki",
        "clientID": "68b4ceb1-f9f8-45c0-bc1f-b40ffcb503c3",
        "clientSecret": "MBPYAYePmQFrzQkw",
        "ownerName": "Shubhanshu Tiwari",
        "ownerEmail": "sa5597@srmist.edu.in",
        "rollNo": "RA2111003010163"
    }
    response = request_for_authorize(url, data)
    if response:
        responseSave(response, "auth_token.json")


if __name__ == "__main__":
    main()