from django.shortcuts import render,HttpResponse , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    return render(request,'forum/home.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        myuser = User.objects.create_user(username, email,password)
        myuser.fname = fname
        myuser.lname = lname
        myuser.save()
        return redirect('index')


    return render(request,'forum/register.html')

def signin(request):
    if request.method == 'POST':
        siginusername = request.POST['siginusername']
        signinpassword = request.POST['signinpassword']
        user = authenticate(username = siginusername, password = signinpassword)
        login(request, user)
        return redirect('index')
    return render(request,'forum/signin.html')

def signout(request):
    logout(request)
    return redirect('index')