from flask import Flask, jsonify
import requests
import threading
import time

app = Flask(__name__)


numbers = []
window_size = 10   #Given
lock = threading.Lock()

def fetch_numbers(number_type):
    g_url = "http://20.244.56.144/test/"
    urls = {
        "e": g_url + "even",
        "f": g_url + "fibo",
        "p": g_url + "primes",
        "r": g_url + "rand"
    }

    url = urls.get(number_type)
    if not url:
        print("Invalid number type.")
        return []

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get("numbers", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching numbers: {e}")
        return []

def avgCalculator(nums):
    if not nums:
        return 0
    return sum(nums) / len(nums)

def update_numbers(new_numbers):
    global numbers
    with lock:
        numbers.extend(new_numbers)
        if len(numbers) > window_size:
            numbers = numbers[-window_size:]

def get_window_state():
    with lock:
        return numbers[-window_size:], numbers[:-window_size]

@app.route('/numbers/<string:number_type>')
def get_numbers(number_type):
    global numbers
    url = f"http://20.244.56.144/test/{number_type}"
    new_numbers = fetch_numbers(url)

    update_numbers(new_numbers)
    window_curr_state, window_preview_state = get_window_state()
    avg = avgCalculator(window_curr_state)

    dataInresponse = {
        "windowPreviewState": window_preview_state,
        "windowCurrState": window_curr_state,
        "numbers": numbers,
        "avg": round(avg, 2)
    }
    return jsonify(dataInresponse)

#To run
if __name__ == '__main__':
    app.run(host='localhost', port=9876, debug=True)
