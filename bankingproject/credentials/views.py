
from django.shortcuts import render
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from bankingapp.models import Formss


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['Password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('login')
        else:
            messages.info(request, "successfully")
            return redirect('/')
    return render(request, "login.html")
def register(request):
    if request.method=='POST':
        Username = request.POST.get('username')
        Password = request.POST['Password']
        Cpassword = request.POST.get('Cpassword')
        user = auth.authenticate(username=Username, password=Password,Cpassword=Cpassword)
        if user is not None:
         auth.login(request, user)
         return redirect('login')
        else:
         messages.info(request, "successfully")
        return redirect('/')
    return render(request, "register.html")


def logout(request):
        auth.logout(request)
        return redirect('/')
def form(request):
    if request.method=='POST':
        name = request.POST.get('name')
        dob  =request.POST.get('dob')
        age =request.POST.get('age')
        gender=request.POST.get('gender')
        phoneNumber=request.POST.get('phoneNumber')
        email=request.POST.get('email')
        address=request.POST.get('address')
        district=request.POST.get('district')
        branch=request.POST.get('branch')
        account_type=request.POST.get('account')
        materials_provide=request.POST.get('materials')
        return redirect('/')
    return render(request, "form.html")

# Create your views here.
