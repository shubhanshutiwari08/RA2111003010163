import requests
import json
import logging

# creating   the  logger to debugg
logging.basicConfig(level=logging.INFO)


def request_for_register(url, data):
    try:
        response = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error("Error making POST request: %s", e)
        return None


def saving_response(response, notebook_filename):
    try:
        with open(notebook_filename, 'w') as notebook_file:
            json.dump(response, notebook_file, indent=4)
        logging.info("Response saved to %s", notebook_filename)
    except IOError as e:
        logging.error("Error saving response to notebook: %s", e)


def main():
    url = "http://20.244.56.144/test/register"
    data = {
        "companyName": "Meraki",
        "ownerName": "Shubhanshu  Tiwari",
        "rollNo": "RA2111003010163",
        "ownerEmail": "sa5597@srmist.edu.in",
        "accessCode": "bntKpm"
    }
    response = request_for_register(url, data)
    if response:
        saving_response(response, "response_collect.json")


if __name__ == "__main__":
    main()