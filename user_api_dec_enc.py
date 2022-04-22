import requests


url_enc = "http://127.0.0.1:5000/enc"
url_dec = "http://127.0.0.1:5000/dec"
resp = 0
while resp != 1 and resp != 2:
    print("[1] --> Encrypt")
    print("[2] --> Decrypt")
    resp = input("[1] or [2]: ")
    try:
        resp = int(resp)
    except:
        print("Not valid input:")
        resp = 0


if resp == 1:
    txt = input("Text: ")
    key = -1
    while key < 0:
        key = input("Key: ")
        try:
            key = int(key)
        except:
            key = -1
    url_total = f"{url_enc}/{txt}/{key}"
    response = requests.get(url_total)
    print(response.json())


if resp == 2:
    txt = input("Text: ")
    key = -1
    while key < 0:
        key = input("Key: ")
        try:
            key = int(key)
        except:
            key = -1
    url_total = f"{url_dec}/{txt}/{key}"
    response = requests.get(url_total)
    print(response.json())
    