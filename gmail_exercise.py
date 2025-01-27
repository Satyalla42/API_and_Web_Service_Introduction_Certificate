import requests

url = "https://gmail.googleapis.com/gmail/v1/users/sattyx3.sf@gmail.com/messages"

payload = {}
headers = {
  'Authorization': 'Bearer 000'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
