import requests
from crypto import Cryptography
from json import dumps

# # this is transaction details 
transation = {
    "first_name": "zeeshan",
    "last_name": "raza",
    "company": "host",
    "address": "localhost",
    "city": "3000",
    "state": "http",
    "zip_code": "8000",
    "country": "poc",
    "phone_number": "9999999999",
    "payment_method": "credit cart",
    "transaction_type": "save",
    "card_number": "8888888888888888",
    "exp_year": "2023",
    "exp_month": "09",
    "cvv": "098",
    "email": "helloworld@gmail.com",
    "authusername": "tabish",
    "transaction_id": "12768hdy-2wsujjhewefedsdfcuw82-89ddd",
    "amount": "70"
}


# # this is hash genrate key don't change key otherwise does not work
KEY = 'Z_wXA1eKA99N-ddUodDW-LIgWLTsCyYWpcMjeO2vnqk='



# this is our credentials 
secret = "de59610c-b1eb-45ab-8933-b29e591843bc"
key = "dec0dcd2-b946-48e9-854f-7a86f62fae00"
account = "300000"


# we will encrypt our transation for security 
# crypto = Cryptography(KEY)
# encrypted_transaction = crypto.encrypt(dumps(transation))
data = {
    'data': transation
}

# now we will show without token request
res = requests.post(f"http://localhost:8000/transation/add/?secret={secret}&key={key}&account={account}",data=transation)
print(res.text)
