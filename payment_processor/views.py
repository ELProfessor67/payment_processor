from django.shortcuts import HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from access_token.models import UserKeys
from transactions.models import Transactions
from batchs.models import Batchs
from django.db.models import Q
from datetime import datetime, timedelta
from utils.getlastmonth import get_last_7_months
from json import dumps
# from utils.mailer import mailer
from django.conf import settings
from django.core.mail import send_mail as send_email
from access_token.models import UserKeys

def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        
        if user is not None:

            if "team-" in user.last_name:
                owner = user.last_name.split('-')[1]
                user = User.objects.filter(username=owner).first()

            auth_login(request,user)
            return redirect('/transation/list')
        else:
            error = 'Invalid details'
            return render(request,'login.html',{"error":error})
        # print(user)

    return render(request,'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        
        errors = []
        user_exist = User.objects.filter(username=username).exists()
        email_exist = User.objects.filter(email=email).exists()
        if user_exist:
            errors.append('this username is already taken')
            return render(request,'register.html',{"errors":errors})
        if email_exist:
            errors.append('this email is already taken')
            return render(request,'register.html',{"errors":errors})
        
        
        try:
            user = User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
            UserKeys.objects.create(username=username,account_id=user.id*100000)
            
            auth_login(request,user)
            return redirect('/transation/list')
        except Exception as e:
            errors.append(e)
            return render(request,'register.html',{"errors":errors})

    return render(request,'register.html')

def api_management(request):
    user = UserKeys.objects.filter(username=request.user.username).first()
    # print(user)
    return render(request,'api_management.html',{"user":user})


def logoutuser(request):
    logout(request)
    return redirect('/login')

def table(request):
    return render(request,'codes.html')


@login_required(login_url='/login')
def dashboard(request):
    owner = request.user.username
    date = request.GET.get('date')
    tquery = Q()
    tquery &= Q(owner=owner)
    bquery = Q()
    bquery &= Q(owner=owner)
    
    if date:
        today = datetime.now()
        if date == 'today':
            tquery &= Q(created_at__date=today)
            bquery &= Q(date__date=today)
        elif date == 'yesterday':
            yesterday = today - timedelta(days=1)
            tquery &= Q(created_at__date=yesterday)
            bquery &= Q(date__date=yesterday)
        elif date == 'last_7_day':
            last_7_day = today - timedelta(weeks=1)
            tquery &= Q(created_at__range=(last_7_day,today))
            bquery &= Q(date__range=(last_7_day,today))
        elif date == 'last_month':
            last_month = today - timedelta(days=30)
            tquery &= Q(created_at__range=(last_month,today))
            bquery &= Q(date__range=(last_month,today))
        elif date == 'last_6_month':
            last_6_month = today - timedelta(days=180)
            tquery &= Q(created_at__range=(last_6_month,today))
            bquery &= Q(date__range=(last_6_month,today))
        elif date == 'last_year':
            last_year = today - timedelta(days=365)
            tquery &= Q(created_at__range=(last_year,today))
            bquery &= Q(date__range=(last_year,today))

    transactions = Transactions.objects.filter(tquery).values()
    batchs = Batchs.objects.filter(bquery)
    usernames_list = []
    for transaction in transactions:
        if not transaction.get('username') in usernames_list:
            usernames_list.append(transaction.get('username'))
    greeting = {}
    greeting['users'] = len(usernames_list)
    greeting['transactions'] = len(transactions)
    greeting['batchs'] = len(batchs)

    toady = datetime.today()
    today_transaction = Transactions.objects.filter(created_at__date=toady,owner=owner)
    today_batchs = Batchs.objects.filter(date__date=toady,owner=owner)
    greeting['newtransactions'] = len(today_transaction)
    greeting['newbatchs'] = len(today_batchs)

    months = get_last_7_months()
    current_year = datetime.now().year
    graph_data = []
    for i in months:
        transactions = Transactions.objects.filter(owner=owner,created_at__month=i,created_at__year=current_year)
        graph_data.append(len(transactions))
    
    greeting['graph_data'] = dumps(graph_data)

    if date:
        greeting['time'] = " ".join(date.split('_'))
    else:
        greeting['time'] = 'All Data'



    return render(request,'index.html',greeting)




def my_team(request):
    name = request.GET.get('name')
    owner = request.user.username
    last_name = f"team-{owner}"
    query = Q()
    query &= Q(last_name__icontains=last_name)
    if name:
        query &= Q(first_name__icontains = name)

    team = User.objects.filter(query)

    for index,item in enumerate(team):
        password = item.last_name.split('-')[2]
        # print(item.first_name)
        team[index].password = password

    return render(request,'my_team.html',{"team":team})


def my_team_add(request):
    if request.method == 'POST':
        owner = request.user.username
        first_name = request.POST.get('first_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')
        last_name = f"team-{owner}-{password}-{role}"
        username_exist = User.objects.filter(username=username).exists()
        email_exist = User.objects.filter(email=email).exists()
        if username_exist:   
            return render(request,'my_team_add.html',{"error":"This username is already exists"})
        if email_exist:
            return render(request,'my_team_add.html',{"error":"This email is already exists"})


        User.objects.create_user(first_name=first_name,last_name=last_name,email=email,password=password,username=username)
        return redirect('/my/team/')
    return render(request,'my_team_add.html')


def delete_my(request,id):
    user = User.objects.filter(id=id).first()
    owner = request.user.username

    if user.last_name.split('-')[1] != owner:
        return HttpResponse('only owner delete there memeber')
    
    user.delete()

    return redirect('/my/team')



def send_mail(request):
    email = request.GET.get('email')
    username = request.GET.get('username')
    password = request.GET.get('password')
    owner = request.user.first_name
    message = f"your add payment procesor team member you added by {owner} your username is `{username}` and your password is `{password}`"
    subject = 'welcome to Payment Processor'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email, ]
    send_email( subject, message, email_from, recipient_list )
    return redirect('/my/team/')
    



def authorize(request):
    secret = request.GET.get('secret')
    key = request.GET.get('key')
    account_id = request.GET.get('account')

    user = UserKeys.objects.filter(secret=secret,key=key,account_id=account_id).values().first()

    if user is not None:
        return HttpResponse(dumps(user),status=200)
    
    print('user',user)
    
    return HttpResponse('unauthrized user',status=401)