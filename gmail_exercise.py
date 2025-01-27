import requests

url = "https://gmail.googleapis.com/gmail/v1/users/sattyx3.sf@gmail.com/messages"

payload = {}
headers = {
  'Authorization': 'Bearer ya29.a0AXeO80Q8k7q6osFuS9jGSX49I4KZWcJyNppp2redwAZaDUebNfIyukoyb9x-V06dokksipI-ZKt4vSf_BMxY4yb_fFPwbrGDlaTq4ttwLgmyloU71aCbQ42-I0YIMXyleU-qig6y_R-fWefm1U4-Q36dzIRP_3pzCJrmCq4oaCgYKAUwSARASFQHGX2MiDN4BBsfWz8raq5BJhPKiDg0175'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
