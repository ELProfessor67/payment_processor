import requests
from crypto import Cryptography
from json import dumps

# this is transaction details 
transation = {
    "trasnsaction_id": "12768hdy-2wsujjhewefedsdfcuw82-89ddd",
    "description": "this is new transaction 2",
    "timestamp": "",
    "currency": "BIT",
    "payment_method": "debit Card",
    "status": 'complete',
    "amount": "1"
}


# this is hash genrate key don't change key otherwise does not work
KEY = 'Z_wXA1eKA99N-ddUodDW-LIgWLTsCyYWpcMjeO2vnqk='


crypto = Cryptography(KEY)
# first json.dumps transaction and add inside crypto.encrpyt method 
encrypted_transaction = crypto.encrypt(dumps(transation))
data = {
    'data': encrypted_transaction
}

# this is auth token 
token = "40037539-8cd9-495a-bd7f-4e5c8721e3a8"

# now i will show without token request

res = requests.post(f"http://localhost:4000/transation/add/?token={token}",data=data)
print(res.text)