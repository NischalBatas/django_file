from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.core.mail import send_mail


def logins(request):
    if request.method=="POST":
        usernames=request.POST['username']
        passwords=request.POST['password']
        user=authenticate(request,username=usernames,password=passwords)
        if user is not None:
            login(request,user)
            return redirect('index')

    return render(request,'auth/logins.html')

def logouts(request):
    logout(request)
    return redirect('logins')

def signup(request):
    if request.method=="POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            print("successful")
            return redirect('index')
        else:
            print("Unsuccessful")
    else:
        form=SignupForm()
    return render(request,'auth/signup.html',{"form":form})

def list(request):
    list=User.objects.all()
    return render(request,'auth/list.html',{"list":list})

def contact(request):
    if request.method == 'POST':
        subjects = request.POST['subjects']
        messages = request.POST['messagess']

        message_from = request.POST['message_from']

        send_mail(
        subjects,
        messages,
        message_from,
        ['nischal.batash@gmail.com'],
        fail_silently=False,
        )
        return render(request, 'auth/contact.html', {'messages': messages,'message_from':message_from})
    else:
        return render(request, 'auth/contact.html')