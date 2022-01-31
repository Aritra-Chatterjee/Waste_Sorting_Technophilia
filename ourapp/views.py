from django.shortcuts import render,redirect
from.models import  Citizens
from django.contrib.auth.models import User,auth
from django.contrib import messages
from.models import Request
from.models import Feedback


# Create your views here.
def index(request):
    return render(request,'index.html')
def citizenportalhome(request):
    return render(request,'citizen-portal-home.html')
def login(request):
    if request.method=='POST':
        username=request.POST['User Id']
        email=request.POST['email']
        password=request.POST['password']
        if Citizens.objects.filter(email=email).exists():
            messages.info(request,'Email Already Used')
            return redirect('login')
        elif Citizens.objects.filter(username=username).exists():
            messages.info(request,'Username Already Used')
            return redirect('login')
        else:
            citizen=Citizens.objects.create_user(username=username,email=email,password=password)
            citizen.save()
            return  redirect('login')

    return render(request,'login.html')
def req(request):
    
    return render(request,'request.html')

def feedback(request):
    return render(request,'feedback.html')
def thankyou(request):
    return render(request,'thank-you.html')
def about(request):

    return render(request,'about.html')
def collectorlogin(request):
    if request.method=='POST':
        username=request.POST['User Id']
        email=request.POST['email']
        password=request.POST['password']
        
        if Citizens.objects.filter(username=username).exists():
            messages.info(request,'Username Already Used')
            return redirect('collectorlogin')
        else:
            citizen=Citizens.objects.create_user(username=username,email=email,password=password)
            citizen.save()
            return  redirect('collectorlogin')
    return render(request,'login-collector.html')
def collectorportal(request):
    return render(request,'collector-portal.html')
def reqs(request):
    
    return render(request,'requests.html')
def citizendata(request):
    return render(request,'citizen-data.html')
def organic(request):
    return render(request,'organic.html')
def recyclable(request):
    return render(request,'recyclable.html')
def electronic(request):
    return render(request,'electronic.html')
def feedbackdata(request):
    return render(request,'feedback-data.html')



