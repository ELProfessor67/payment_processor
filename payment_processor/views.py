from django.shortcuts import HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from access_token.models import UserKeys

def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
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

def about(request):
    return redirect('/login')