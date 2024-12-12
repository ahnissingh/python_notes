import requests
url = "https://httpbin.org/get"
try:
    response = requests.get(url)
    with open('result.json', 'w', encoding='utf-8') as file:
        file.write(response.text)
        print(f"Wrote json to file ")
except requests.exceptions.RequestException as e:
    print(f"Error {e}")
