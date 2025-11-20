import requests

login_url = "https://employee.isaar.in/api/login"
payload = {
    "employeeCode": "ISARED025039",
    "password": "1234"
}

s = requests.Session()
resp = s.post(login_url, json=payload, timeout=10)

print("Status code:", resp.status_code)
print("Response headers:", resp.headers)
print("Raw response text:\n", resp.text)
