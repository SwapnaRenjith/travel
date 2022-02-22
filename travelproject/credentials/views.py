from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth


def register(request):
    if request.method == 'POST':
        user = request.POST['username']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        passw = request.POST['password']
        cpass = request.POST['password1']
        if passw == cpass:
            if User.objects.filter(username=user).exists():
                messages.info(request,"Username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=user, first_name=fname, last_name=lname, email=email,
                                                password=passw)
                user.save();
                return redirect('login')

            # print("user created")
        else:
            messages.info(request,"password not match")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        user = request.POST['username']
        passw = request.POST['password']
        user=auth.authenticate(username=user,password=passw)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
