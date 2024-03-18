import requests

# Constants
ROLL_NUMBER = "21109920269"
NAME = "Udit"
EMAIL = "udit2026.be21@chitkara.edu.in"
PHONE = "8307550939"
COMPANY = "Bajaj Finserv"

# Create Investment Account
api_url_1 = "https://customer-analytics-34146.my.salesforce-sites.com/services/apexrest/createAccount"
headers_1 = {"Content-Type": "application/json"}
data_1 = {
    "name": NAME,
    "email": EMAIL,
    "rollNumber": ROLL_NUMBER,
    "phone": PHONE,
}
response_1 = requests.post(api_url_1, json=data_1, headers=headers_1)

if response_1.status_code == 200:
    account_number = response_1.json()["accountNumber"]
    print(f"Account created successfully. Account Number: {account_number}")
else:
    print("Failed to create account. Error:", response_1.text)

# Buy Stocks
current_price = "1573"
acc = "BFHL0018620"

api_url_2 = "https://customer-analytics-34146.my.salesforce-sites.com/services/apexrest/buyStocks"
headers_2 = {"content-type": "application/json", "bfhl-auth": ROLL_NUMBER}
data_2 = {
    "company": COMPANY,
    "currentPrice": current_price,
    "accountNumber": acc,
    "githubRepoLink" : "https://github.com/udit-2026/Bajaj-Finserv"
}
response_2 = requests.post(api_url_2, json=data_2, headers=headers_2)

if response_2.status_code == 200:
    print("Stocks purchased successfully.")
else:
    print("Failed to purchase stocks.")
