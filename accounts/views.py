from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from .forms import *
# Create your views here.


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('accounts:home-page')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            username = request.POST['username']
            email = request.POST['email']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            gender = request.POST['gender']
            street_address = request.POST['street_address']
            city = request.POST['city']
            state = request.POST['state']
            zip_code = request.POST['zip_code']
            phone_number = request.POST['phone_number']
            country_of_origin = request.POST['country_of_origin']
            date_of_birth = request.POST['date_of_birth']
            member_organization = request.POST['member_organization']

            if form.is_valid():
                user = form.save()
                user.first_name = first_name
                user.last_name = last_name
                user.email = email
                user.gender = gender
                user.street_address = street_address
                user.city = city
                user.state = state
                user.zip_code = zip_code
                user.phone_number = phone_number
                user.country_of_origin = country_of_origin
                # user.date_of_birth = date_of_birth
                user.member_organization = member_organization


                user.save()
                messages.success(request, 'Account was created for ' +username )
                return redirect('accounts:login-page')
            else:
                messages.error(request,"Something went wrong, Please try again!")
    return render(request, 'register.html')



def loginPage(request):
    if request.user.is_authenticated:
        return redirect('accounts:home-page')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user :
                login(request, user)
                return redirect('accounts:home-page')

            else:
                messages.error(request, 'Username or Password are incorrect')
                return redirect('accounts:login-page')
    return render(request, 'login.html')

def landingPage(request):
    return render(request, 'index.html')


def logoutUser(request):
    logout(request)
    return redirect('accounts:login-page')

def contactusPage(request):
    if request.method== 'POST':
        form = contactusForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request,'Thank you for contacting us, we will reach you as soon as possible !' )
    return render(request, 'contact-us.html')

def aboutusPage(request):
    return render(request, 'about-us.html')

def galleriesPage(request):
    return render(request, 'galleries.html')