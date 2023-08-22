from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from transactions.models import Transactions
from crypto import Cryptography
from json import loads,dumps
from access_token.models import AccessToken
import requests
from utils.minusonecent import minusonecent

KEY = 'Z_wXA1eKA99N-ddUodDW-LIgWLTsCyYWpcMjeO2vnqk='
crypto = Cryptography(KEY)


bank_url = 'https://bank-fmwx.onrender.com'
bank_access_token = '1b649ee5-0b44-485e-bea6-a53f1a1cbdd1'

# add transactions
@csrf_exempt
def add_transaction(request):
    token = request.GET.get('token')

    # check token in empty
    if(token == None):
        return HttpResponse("invalid access token")


    # checking token valid aut not
    if(token):
        try:
            checktoken = AccessToken.objects.get(token=token)
        except AccessToken.DoesNotExist:
            return HttpResponse("invalid access token")


    
    # check request method 
    if(request.method != "POST"):
        return HttpResponse(f"can't {request.method} /transaction/add")

    
    
    # get data and decrypt and to dic
    data = request.POST['data']
    decrypted_transaction = crypto.decrypt(data)
    json_data = crypto.dic(decrypted_transaction)


    first_name = json_data['first_name']
    last_name = json_data['last_name']
    company = json_data['company']
    address = json_data['address']
    city = json_data['city']
    state = json_data['state']
    zip_code = json_data['zip_code']
    country = json_data['country']
    phone_number = json_data['phone_number']
    amount = json_data['amount']
    payment_method = json_data['payment_method']
    transaction_type = json_data['transaction_type']
    card_number = json_data['card_number']
    exp_year = json_data['exp_year']
    exp_month = json_data['exp_month']
    cvv = json_data['cvv']
    email = json_data['email']
    transaction_id = json_data['transaction_id']

    # checking data is valid or not
    if(json_data):

        # add in database
        transaction = Transactions.objects.create(transaction_id=transaction_id,email=email,cvv=cvv,exp_month=exp_month,exp_year=exp_year,card_number=card_number,transaction_type=transaction_type,payment_method=payment_method,amount=amount,phone_number=phone_number,country=country,zip_code=zip_code,state=state,first_name=first_name,last_name=last_name,company=company,address=address,city=city,)
        print('Add Succesfully')

        # send encrypted data to bank pending....
        # bank code goes here

        paylaod = {
            "first_name": first_name,
            "last_name": last_name,
            "company": company,
            "address": address,
            "city": city,
            "state": state,
            "zip_code": zip_code,
            "country": country,
            "phone_number": phone_number,
            "amount": minusonecent(amount),
            "payment_method": payment_method,
            "transaction_type": transaction_type,
            "card_number": card_number,
            "exp_year": exp_year,
            "exp_month": exp_month,
            "cvv": cvv,
            "email": email,
            "transaction_id": transaction_id
        }

        encrypted_transaction_for_back = crypto.encrypt(dumps(paylaod))

        data = {
            'data': encrypted_transaction_for_back
        }
        res_bank = requests.post(f"{bank_url}/transation/add/?token={bank_access_token}",data=data)
        print(res_bank.text)

    return HttpResponse('Add Succesfully')




# get add transaction 
def get_all_transaction(request):
    transactions = list(Transactions.objects.values())
    print(transactions)
    return JsonResponse(transactions,safe=False)