from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user =auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
                return render(request,'login.html',{'error':'username or password is incorrect'})

    else:    
                return render(request,'login.html')


def signup(request):
    if request.method == 'POST':
       if request.POST['password1']==request.POST['password2']:
           user=User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
           auth.login(request,user)
           
           return redirect('blog')
    return render(request,'signup.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        redirect('home')
        return render(request,'login.html')