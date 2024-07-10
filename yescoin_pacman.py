import requests
import json
import random
import time

url = 'https://api-backend.yescoin.gold/game/collectCoin'

headers_base = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126", "Microsoft Edge WebView2";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'Referer': 'https://www.yescoin.gold/',
    'Referrer-Policy': 'strict-origin-when-cross-origin'
}

# Function to read tokens from file
def read_tokens_from_file(filename):
    with open(filename, 'r') as f:
        tokens = [line.strip() for line in f.readlines() if line.strip()]
    return tokens

# Read tokens from file
tokens = read_tokens_from_file('tokens.txt')

while True:  # Infinite loop to continuously perform the operation
    for token in tokens:
        headers = headers_base.copy()
        headers['token'] = token

        # Generate a random collectAmount (assuming a range from 100 to 1000)
        collectAmount = random.randint(100, 1000)

        data = json.dumps(str(collectAmount))  # Convert collectAmount to JSON format

        try:
            response = requests.post(url, headers=headers, data=data)
            response_data = response.json()
            if response_data['code'] == 0:
                print(f"collectAmount: {response_data['data']['collectAmount']}")  # Assuming the response is JSON and you want to print it
            elif response_data['code'] == 400003:
                print(response_data['message'])
        except Exception as e:
            print(f"An error occurred: {e}")

        # Optional: Add a delay between requests
        time.sleep(1)  # Adjust the delay (in seconds) as needed

    print("~" * 20)  # Print an empty line for separation between complete iterations
# Main function to read tokens and perform tasks indefinitely
# Note: Use caution with infinite loops, especially when making network requests.
# Ensure that you have appropriate error handling and rate limiting to avoid issues.
