import requests

url = "https://www.voanews.com/"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
}

res = requests.get(url=url, headers=headers)
print(res)
