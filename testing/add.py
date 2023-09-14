import requests
from crypto import Cryptography
from json import dumps

# # this is transaction details 
# transation = {
#     "trasnsaction_id": "12768hdy-2wsujjhewefedsdfcuw82-89ddd",
#     "description": "this is new transaction 2",
#     "timestamp": "",
#     "currency": "BIT",
#     "payment_method": "debit Card",
#     "status": 'complete',
#     "amount": "1"
# }


# # this is hash genrate key don't change key otherwise does not work
# KEY = 'Z_wXA1eKA99N-ddUodDW-LIgWLTsCyYWpcMjeO2vnqk='


# crypto = Cryptography(KEY)
# # first json.dumps transaction and add inside crypto.encrpyt method 
# encrypted_transaction = crypto.encrypt(dumps(transation))
# data = {
#     'data': encrypted_transaction
# }

# # this is auth token 
# token = "40037539-8cd9-495a-bd7f-4e5c8721e3a8"

# # now i will show without token request

# res = requests.post(f"http://localhost:4000/batch/create/?token={token}",data=data)
# print(res.text)

# bank_url = 'https://bank-fmwx.onrender.com'
payment_process_url = 'http://localhost:4000'
payment_process_access_token = "27be761f-1046-49b0-be1f-35a678a41781"
gateway_url = 'http://localhost:8000'
batch_id = 18

data = {
    'status': 'Complete'
}

res_process = requests.post(f"{payment_process_url}/batch/change_status/{batch_id}?token={payment_process_access_token}",data=data)
res_gateway = requests.post(f"{gateway_url}/projects/change_status/{batch_id}",data=data)
print(res_gateway.text,res_process.text)
