import requests

def send_request(number_type):
    url = f"http://localhost:9876/numbers/{number_type}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error sending request: {e}")
        return None

if __name__ == "__main__":
    valid_types = ['e', 'f', 'p', 'r']
    number_type = input(f"Enter the number type ({', '.join(valid_types)}): ")
    
    if number_type not in valid_types:
        print("Invalid number type.")
    else:
        response = send_request(number_type)
        if response:
            print("Response:")
            print(response)