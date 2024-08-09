import requests
import json
import random
import time
import pyfiglet

def print_banner():
    result = pyfiglet.figlet_format('Yescoin')
    print(result)
    print("\nScript By : @abiedarmawan\n")
    print("-" * 40)

def count_lines(filename):
    with open(filename, 'r') as file:
        return sum(1 for line in file if line.strip())

def read_tokens_from_file(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def balance(token, headers_base):
    headers = headers_base.copy()
    headers['token'] = token
    url_info = "https://api-backend.yescoin.gold/account/getAccountInfo"
    response = requests.get(url_info, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        userId = data["data"]["userId"]
        currentAmount = data["data"]["currentAmount"]
        print(f"userId: {userId}")
        print(f"jumlah yescoin: {currentAmount}")
    else:
        print(f"Failed with status code {response.status_code}")

def tampilkan_urutan_tokens(token, index):
    print("~" * 5, f"Akun {index + 1}", "~" * 5,)

def collect_coins(token, headers_base):
    headers = headers_base.copy()
    headers['token'] = token
    url = 'https://api-backend.yescoin.gold/game/collectCoin'
    collectAmount = random.randint(1, 1000)
    data = json.dumps(str(collectAmount))
    try:
        response = requests.post(url, headers=headers, data=data)
        response_data = response.json()
        if response_data['code'] == 0:
            print(f"collectAmount: {response_data['data']['collectAmount']}")
        elif response_data['code'] == 400003:
            print(response_data['message'])
    except Exception as e:
        print(f"An error occurred: {e}")

def countdown(seconds):
    for i in range(seconds, -1, -1):
        minutes, secs = divmod(i, 60)
        print(f'Next run in {minutes:02}:{secs:02}', end='\r')
        time.sleep(1)
    print('')

def main():
    print_banner()
    token_file = 'tokens.txt'
    line_count = count_lines(token_file)
    print(f"Total jumlah akun: {line_count}")
    print("-" * 40)

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

    tokens = read_tokens_from_file(token_file)
    interval = 30  # Set countdown interval (in seconds)

    while True:
        for index, token in enumerate(tokens):
            tampilkan_urutan_tokens(token, index)
            balance(token, headers_base)
            collect_coins(token, headers_base)
            time.sleep(random.uniform(1, 3))  # Adjust sleep duration as needed
        countdown(interval)
        print("~" * 20)

if __name__ == "__main__":
    main()
