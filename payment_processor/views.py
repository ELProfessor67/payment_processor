from django.shortcuts import HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout

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

def logoutuser(request):
    logout(request)
    return redirect('/login')

def table(request):
    return render(request,'codes.html')

def about(request):
    return redirect('/login')