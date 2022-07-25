from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import CreateUserForm
from .models import *

def index(request):
    context = {
        
    }
    return render(request, 'index.html', context)



# Sign up
def sign_up(request):
    first = CreateUserForm()
    if request.method == 'POST':
        first = CreateUserForm(request.POST)
        if first.is_valid():
            first.save()
            return redirect('sign_in')
        else:
            messages.info(request, 'e-mail pocta öň registrasiýa edilen')
    return render(request, 'sign_up.html', {'first': first})

# Sign in
def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            print("slam")
            return redirect('end')
        else:
            messages.info(
                request, 'Ulanyjy e-mail poctanyzda ýa-da parolyňyzda ýalňyşlyk goýberdiňiz barlaň!')
    context = {}
    return render(request, 'sign_in.html', context)


# End
def end(request):
    context = {}
    return render(request, 'end.html', context)


# Logout
def logout_page(request):
    logout(request)
    return redirect('/')

