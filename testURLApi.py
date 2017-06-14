import requests, json

url = "http://127.0.0.1:8080/predict"

data = 	{[190,70,43]}

r = requests.post(url, data)

print(r.text)