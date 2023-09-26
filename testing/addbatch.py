import requests
from crypto import Cryptography
from json import dumps

# # this is transaction details 
batch = {
    "name": "zeeshan",
    "desciption": "desciption",
    "username": "tabish",
    "transactions": dumps(['12768hdy-2wsujjhewefedsdfcuw82-89ddd']),
    "batch_id": 1,
    "status": 'Pending'
}

# this is our credentials 
secret = "de59610c-b1eb-45ab-8933-b29e591843bc"
key = "dec0dcd2-b946-48e9-854f-7a86f62fae00"
account = "300000"


# now we will show without token request
res = requests.post(f"http://localhost:8000/batch/create/?secret={secret}&key={key}&account={account}",data=batch)
print(res.text)