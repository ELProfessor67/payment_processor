from django.shortcuts import render, HttpResponse
from access_token.models import AccessToken
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from crypto import Cryptography
from .models import Batchs
from json import dumps, loads
from transactions.models import Transactions
import requests
from django.db.models import Q
from access_token.models import UserKeys
# Create your views here.

KEY = 'Z_wXA1eKA99N-ddUodDW-LIgWLTsCyYWpcMjeO2vnqk='
crypto = Cryptography(KEY)

# bank_url = 'https://bank-fmwx.onrender.com'
bank_url = 'http://localhost:3000'
bank_access_token = '1b649ee5-0b44-485e-bea6-a53f1a1cbdd1'

@csrf_exempt
def create_batch(request):
    secret = request.GET.get('secret')
    key = request.GET.get('key')
    account = request.GET.get('account')
    print('aaye','aaaaaa yyaaaayayyayayay')

    owner = UserKeys.objects.filter(secret=secret,key=key,account_id=account).first()
    print(owner.username)
    # check token in empty
    if(owner == None):
        return HttpResponse("invalid credentials",status=401)

    
    # check request method 
    if(request.method != "POST"):
        return HttpResponse(f"can't {request.method} /batch/create",status=404)

    
    
    # get data and decrypt and to dic
    # data = request.POST['data']
    # bacths_decrypted = crypto.decrypt(data)
    # json_data = crypto.dic(bacths_decrypted)
    json_data = request.POST

    name = json_data.get('name')
    desciption = json_data.get('desciption')
    username =json_data.get('username')
    transactions = json_data.get('transactions')
    status = json_data.get('status')
    date = json_data.get('date')
    batch_id = json_data.get('batch_id')
    # print(status,name)
    # checking data is valid or not
    print(json_data)
    if(json_data):

        # add in database
        batch = Batchs(owner=owner.username,batch_id=batch_id,name=name,desciption=desciption,username=username,transactions=transactions,status=status)
        batch.save()
        print(batch)
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
            "batch_id": batch_id,
            "owner": owner.username
        }

        excrypted_batchs = crypto.encrypt(dumps(paylaod))

        data = {
            'data': excrypted_batchs
        }
        try:
            res_bank = requests.post(f"{bank_url}/batch/create/?token={bank_access_token}",data=data)
            print(res_bank.text)
        except Exception as e:
            print(e)

        return HttpResponse('Add Succesfully',status=201)
    
    return HttpResponse('Invalid details',status=404)
    

@login_required(login_url='/login')
def batch_list(request):
    owner = request.user.username
    start = request.GET.get('start')
    end = request.GET.get('end')
    name = request.GET.get('name')

    query = Q()
    query &= Q(owner=owner)
    if start and end:
        if start == end:
            query &= Q(date__date=start)
        else:
            query &= Q(date__range=(start,end))
    
    if name:
        query &= Q(username__icontains = name)

    
    batchs = Batchs.objects.filter(query).values()

    all_sale_transaction_card = []
    all_credit_trsansaction_card = []
        
    for i in range(len(batchs)):
        trasnsactions_ids = loads(batchs[i].get('transactions'))
        total = 0
        credit = 0
        sales = 0
        for id in trasnsactions_ids:
            print(id)
            transaction = Transactions.objects.filter(transaction_id=id).first()
            if transaction.transaction_type == 'refund':
                all_credit_trsansaction_card.append(transaction.get_card_company())
            else:
                all_sale_transaction_card.append(transaction.get_card_company())
                
            if transaction.transaction_type == 'refund':
                credit += int(transaction.amount)
            else:
                sales += int(transaction.amount)

            total += int(transaction.amount)
        batchs[i]['total'] = total
        batchs[i]['sales'] = sales
        batchs[i]['credit'] = credit

    all_sale_transaction_card_data = {}
    all_credit_trsansaction_card_data = {}
    for i in all_sale_transaction_card:
        if i in all_sale_transaction_card_data:
            all_sale_transaction_card_data[i] += 1
        else:
            all_sale_transaction_card_data[i] = 1
        
    for i in all_credit_trsansaction_card:
        if i in all_credit_trsansaction_card_data:
            all_credit_trsansaction_card_data[i] += 1
        else:
            all_credit_trsansaction_card_data[i] = 1
    
    greeting = {}
    greeting['credit_data'] = dumps(all_credit_trsansaction_card_data)
    greeting['sale_data'] = dumps(all_sale_transaction_card_data)
    greeting['batchs'] = batchs

    return render(request, 'batchs_list.html',greeting)


@login_required(login_url='/login')
def batch_transaction_list(request,id):
    owner = request.user.username
    start = request.GET.get('start')
    end = request.GET.get('end')
    name = request.GET.get('name')

    query = Q()
    query &= Q(owner=owner)
    if start and end:
        if start == end:
            query &= Q(created_at__date=start)
        else:
            query &= Q(created_at__range=(start,end))
    
    if name:
        query &= Q(first_name__icontains = name)

    batchs = Batchs.objects.filter(id=id).values().first()
    transaction_ids = loads(batchs.get('transactions'))

    transactions = []
    for transaction_id in transaction_ids:
        query &= Q(transaction_id=transaction_id)
        transaction = Transactions.objects.filter(query).first()
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