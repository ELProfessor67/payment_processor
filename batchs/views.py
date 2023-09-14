from django.shortcuts import render, HttpResponse
from access_token.models import AccessToken
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from crypto import Cryptography
from .models import Batchs
from json import dumps, loads
from transactions.models import Transactions
import requests
# Create your views here.

KEY = 'Z_wXA1eKA99N-ddUodDW-LIgWLTsCyYWpcMjeO2vnqk='
crypto = Cryptography(KEY)

# bank_url = 'https://bank-fmwx.onrender.com'
bank_url = 'http://localhost:3000'
bank_access_token = '1b649ee5-0b44-485e-bea6-a53f1a1cbdd1'

@csrf_exempt
def create_batch(request):
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
    bacths_decrypted = crypto.decrypt(data)
    json_data = crypto.dic(bacths_decrypted)

    name = json_data.get('name')
    desciption = json_data.get('desciption')
    username =json_data.get('username')
    transactions = json_data.get('transactions')
    status = json_data.get('status')
    date = json_data.get('date')
    batch_id = json_data.get('batch_id')
    # print(status,name)
    # checking data is valid or not
    if(json_data):

        # add in database
        batch = Batchs(batch_id=batch_id,date=date,name=name,desciption=desciption,username=username,transactions=transactions,status=status)
        batch.save()
        print('Add Succesfully')

        # send encrypted data to bank pending....
        # bank code goes here

        paylaod = {
            "name" : name,
            "desciption" : desciption,
            "username" : username,
            "transactions" : transactions,
            "status" : status,
            "date":date,
            "batch_id": batch_id
        }

        excrypted_batchs = crypto.encrypt(dumps(paylaod))

        data = {
            'data': excrypted_batchs
        }
        res_bank = requests.post(f"{bank_url}/batch/create/?token={bank_access_token}",data=data)
        print(res_bank.text)

    return HttpResponse('Add Succesfully')

@login_required(login_url='/login')
def batch_list(request):
    batchs = Batchs.objects.all().values()
    return render(request, 'batchs_list.html',{"batchs":batchs})


@login_required(login_url='/login')
def batch_transaction_list(request,id):
    batchs = Batchs.objects.filter(id=id).values().first()
    transaction_ids = loads(batchs.get('transactions'))

    transactions = []
    for transaction_id in transaction_ids:
        transaction = Transactions.objects.filter(transaction_id=transaction_id).first()
        if transaction != None:
            transactions.append(transaction)
    
    if batchs == None:
        return HttpResponse('invalid batchh id')
    
    temp_transactions = []
    for i in transactions:
        temp_transactions.append(i.get_codes().cut_fee())
    transactions = temp_transactions

    
    return render(request,'user_all_transaction.html',{'transactions':transactions})
    # return HttpResponse(str(transactions))


@csrf_exempt
def change_status(request,id):
    status = request.POST.get('status')
    batch = Batchs.objects.filter(batch_id=id).first()
        
    if batch == None:
        return HttpResponse('Invalid batch Id')
        
    batch.status = status
    batch.save()
    return HttpResponse('change successfully')