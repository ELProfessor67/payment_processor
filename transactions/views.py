from django.http import JsonResponse,HttpResponse
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from transactions.models import Transactions,Fees
from crypto import Cryptography
from json import loads,dumps
from access_token.models import AccessToken, UserKeys
import requests
from utils.minusonecent import minusonecent
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User

KEY = 'Z_wXA1eKA99N-ddUodDW-LIgWLTsCyYWpcMjeO2vnqk='
# KEY = os.environ.get('encryption_key')
crypto = Cryptography(KEY)


def add_transactions(request):
    secret = request.GET.get('secret')
    key = request.GET.get('key')
    account = request.GET.get('account')

    owner = UserKeys.objects.filter(secret=secret,key=key,account_id=account).first()
    print(owner.username)
    # check token in empty
    if(owner == None):
        return HttpResponse("invalid credentials",status=401)

    
    # check request method 
    if(request.method != "POST"):
        return HttpResponse(f"can't {request.method} /transaction/add",status=404)

    
    
 
    json_data = request.POST
    encrypted_transaction = crypto.encrypt(json_data)
    # encrypt transaction
   

    if(json_data):

        # add in database
        transaction = Transactions.objects.create(owner = ownername,transaction=encrypted_transaction)
        print('Add Succesfully')

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
        username = json_data['authusername']
        ownername = owner.username

        # send encrypted data to bank pending....
        # bank code goes here
        print(amount)
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
            "avaible_amount": minusonecent(amount),
            "payment_method": payment_method,
            "transaction_type": transaction_type,
            "card_number": card_number,
            "exp_year": exp_year,
            "exp_month": exp_month,
            "cvv": cvv,
            "email": email,
            "transaction_id": transaction_id,
            "fees": int(amount)/100,
            "total_amount": amount,
            "username": username
        }

        encrypted_transaction_for_back = crypto.encrypt(dumps(paylaod))

        data = {
            'data': encrypted_transaction_for_back
        }
        try:
            res_bank = requests.post(f"{bank_url}/transation/add/?token={bank_access_token}",data=data)
            print(res_bank.text)
        except Exception as e:
            print(e)
        

    return HttpResponse('Add Succesfully',status=201)





# bank_url = 'https://bank-fmwx.onrender.com'
bank_url = 'http://localhost:3000'
bank_access_token = '1b649ee5-0b44-485e-bea6-a53f1a1cbdd1'

# add transactions
@csrf_exempt
def add_transaction(request):
    secret = request.GET.get('secret')
    key = request.GET.get('key')
    account = request.GET.get('account')

    owner = UserKeys.objects.filter(secret=secret,key=key,account_id=account).first()
    print(owner.username)
    # check token in empty
    if(owner == None):
        return HttpResponse("invalid credentials",status=401)

    
    # check request method 
    if(request.method != "POST"):
        return HttpResponse(f"can't {request.method} /transaction/add",status=404)

    
    
    # get data and decrypt and to dic
    # data = request.POST.get('data')
    # print('data',request.POST['amount'])
    json_data = request.POST
    # decrypted_transaction = crypto.decrypt(data)
    # json_data = crypto.dic(decrypted_transaction)
   

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
    username = json_data['authusername']
    ownername = owner.username
    # print('json data',json_data)
    # checking data is valid or not
    if(json_data):

        # add in database
        transaction = Transactions.objects.create(owner = ownername,username=username,transaction_id=transaction_id,email=email,cvv=cvv,exp_month=exp_month,exp_year=exp_year,card_number=card_number,transaction_type=transaction_type,payment_method=payment_method,amount=amount,phone_number=phone_number,country=country,zip_code=zip_code,state=state,first_name=first_name,last_name=last_name,company=company,address=address,city=city,)
        print('Add Succesfully')

        # send encrypted data to bank pending....
        # bank code goes here
        print(amount)
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
            "avaible_amount": minusonecent(amount),
            "payment_method": payment_method,
            "transaction_type": transaction_type,
            "card_number": card_number,
            "exp_year": exp_year,
            "exp_month": exp_month,
            "cvv": cvv,
            "email": email,
            "transaction_id": transaction_id,
            "fees": int(amount)/100,
            "total_amount": amount,
            "username": username
        }

        encrypted_transaction_for_back = crypto.encrypt(dumps(paylaod))

        data = {
            'data': encrypted_transaction_for_back
        }
        try:
            res_bank = requests.post(f"{bank_url}/transation/add/?token={bank_access_token}",data=data)
            print(res_bank.text)
        except Exception as e:
            print(e)
        

    return HttpResponse('Add Succesfully',status=201)




# get add transaction 
def get_all_transaction(request):
    transactions = list(Transactions.objects.values())
    print(transactions)
    return JsonResponse(transactions,safe=False)



@login_required(login_url='/login')
def user_show_list(request):
    owner = request.user.username
    name = request.GET.get('name')
    start = request.GET.get('start')
    end = request.GET.get('end')
    query = Q()
    query &= Q(owner=owner)

    if start and end:
        if start == end:
            query &= Q(created_at__date=start)
        else:
            query &= Q(created_at__range=(start,end))
    
    if name:
        query &= Q(username__icontains=name)


    transactions = Transactions.objects.filter(query).values()

    usernames_list = []
    for transaction in transactions:
        if not transaction.get('username') in usernames_list:
            usernames_list.append(transaction.get('username'))
    
    list = []
    for username in usernames_list:
        user_transation = Transactions.objects.filter(username=username,owner=owner).values()
        list_user_transation = []
        for t in user_transation:
            list_user_transation.append(t)

        obj = {
            "username": username,
            "total_transaction": len(user_transation),
            "last_transaction": user_transation[len(user_transation)-1].get('created_at')
        }
        list.append(obj)
    
    return render(request,'transaction_user_list.html',{'list':list})


@login_required(login_url='/login')
def user_transaction(request,username):
    name = request.GET.get('name')
    start = request.GET.get('start')
    end = request.GET.get('end')
    
    query = Q()
    query &= Q(owner=request.user.username)
    query &= Q(username=username)

    if start and end:
        if start == end:
            query &= Q(created_at__date=start)
        else:
            query &= Q(created_at__range=(start,end))
    
    if name:
        query &= Q(first_name__icontains=name)

    transactions = Transactions.objects.filter(query)
    temp_transactions = []
    for i in transactions:
        temp_transactions.append(i.get_codes().cut_fee())
    transactions = temp_transactions

    # print(transactions[0].codes)

    return render(request,'user_all_transaction.html',{'transactions':transactions})

@login_required(login_url='/login')
def fee(request):
    if not request.user.is_superuser:
        return redirect('/')
    
    username = request.GET.get('username')
    users = User.objects.all()

    temp = []
    for i in users:
        print(i.is_superuser)
        if 'team-' not in i.last_name:
            if not i.is_superuser:
                temp.append(i)
    
    users = temp

    fee_model = Fees.objects.filter(username=username).first()
    if fee_model == None:
        fee_model = {}
        fee_model['percent'] = 2.5
        fee_model['flat_fee'] = 0.5

    if request.method == "POST":
        percent = request.POST.get('percent')
        flat_fee = request.POST.get('flat_fee')
        username = request.POST.get('username')
        # if fee_model is None:
        #     fee_model = Fees.objects.create(percent=percent,flat_fee=flat_fee)
        # else:
        #     fee_model.percent = percent
        #     fee_model.flat_fee = flat_fee
        #     fee_model.save()
        # print(fee_model)
        # print(flat_fee,percent)
        user = Fees.objects.filter(username=username).first()
        if user != None:
            user.flat_fee = flat_fee
            user.percent = percent
            user.save()
        else:
            Fees.objects.create(percent=percent,flat_fee=flat_fee,username=username)

        return redirect(f"/transation/fee/?username={username}")
    print(fee_model)
    return render(request,'customize_fee.html',{"model":fee_model,'users':users,'username':username})



@login_required(login_url='/login')
def all_trasnactions(request):
    name = request.GET.get('name')
    start = request.GET.get('start')
    end = request.GET.get('end')
    owner = request.user.username

    query = Q()
    query &= Q(owner=owner)

    if start and end:
        if start == end:
            query &= Q(created_at__date=start)
        else:
            query &= Q(created_at__range=(start,end))
    
    if name:
        query &= Q(first_name__icontains=name)
    
    transactions = Transactions.objects.filter(query)

    temp = []

    for i in transactions:
        temp.append(i.get_codes().cut_fee())
    
    transactions = temp
    return render(request,'user_all_transaction.html',{'transactions':transactions})